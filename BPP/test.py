import random
import time
import matplotlib.pyplot as plt


class Item:
    def __init__(self, indice, peso):
        self.indice = indice
        self.peso = peso


class Bin:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.itens = []
        self.peso_atual = 0

    def adicionar_item(self, item):
        if self.peso_atual + item.peso <= self.capacidade:
            self.itens.append(item)
            self.peso_atual += item.peso
            return True
        return False

    def __repr__(self):
        return f"Bin(capacidade={self.capacidade}, peso_atual={self.peso_atual}, itens={self.itens})"


class GGA:
    def __init__(self, data, population_size=100, generations=100, mutation_rate=0.1):
        self.bin_size = data["bin_capacity"]
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.itens = [Item(indice, peso)
                      for indice, peso in enumerate(data["weights"])]
        self.itens.sort(key=lambda x: x.peso, reverse=True)
        self.population = self.initialize_population()
        self.fitness = []

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            solucao = list(range(len(self.itens)))
            random.shuffle(solucao)
            population.append(solucao)
        return population

    def evaluate_fitness(self, solucao):
        bins = []
        bin_atual = Bin(self.bin_size)

        for item_index in solucao:
            item = self.itens[item_index]
            if not bin_atual.adicionar_item(item):
                bins.append(bin_atual)
                bin_atual = Bin(self.bin_size)
                bin_atual.adicionar_item(item)

        if bin_atual.itens:
            bins.append(bin_atual)

        return len(bins)

    def selection(self):
        tournament_size = 3
        selected = []
        for _ in range(self.population_size):
            tournament = random.sample(self.population, tournament_size)
            tournament_fitness = [self.evaluate_fitness(
                solucao) for solucao in tournament]
            selected.append(
                tournament[tournament_fitness.index(min(tournament_fitness))])
        return selected

    def crossover(self, pai1, pai2):
        """
        Realiza o cruzamento (crossover) usando Order Crossover (OX).
        """
        ponto_corte1 = random.randint(0, len(pai1) - 2)
        ponto_corte2 = random.randint(ponto_corte1 + 1, len(pai1) - 1)

        filho1 = [-1] * len(pai1)
        filho2 = [-1] * len(pai1)

        # Copia a seção intermediária
        filho1[ponto_corte1:ponto_corte2] = pai1[ponto_corte1:ponto_corte2]
        filho2[ponto_corte1:ponto_corte2] = pai2[ponto_corte1:ponto_corte2]

        # Preenche os espaços vazios mantendo a ordem
        i = j = ponto_corte2
        while -1 in filho1:
            if pai2[j % len(pai2)] not in filho1:
                filho1[i % len(filho1)] = pai2[j % len(pai2)]
                i += 1
            j += 1

        i = j = ponto_corte2
        while -1 in filho2:
            if pai1[j % len(pai1)] not in filho2:
                filho2[i % len(filho2)] = pai1[j % len(pai1)]
                i += 1
            j += 1

        return filho1, filho2

    def mutate(self, solucao):
        """
        Realiza a mutação em uma solução.
        """
        for i in range(len(solucao)):
            if random.random() < self.mutation_rate:
                j = random.randint(0, len(solucao) - 1)
                solucao[i], solucao[j] = solucao[j], solucao[i]
        return solucao

    def run(self):
        best_fitness_over_time = []
        for generation in range(self.generations):
            self.fitness = [self.evaluate_fitness(
                solucao) for solucao in self.population]
            new_population = []
            selected = self.selection()
            for i in range(0, self.population_size, 2):
                pai1, pai2 = selected[i], selected[i + 1]
                filho1, filho2 = self.crossover(pai1, pai2)
                new_population.append(self.mutate(filho1))
                new_population.append(self.mutate(filho2))
            self.population = new_population
            best_fitness = min(self.fitness)
            best_fitness_over_time.append(best_fitness)
            print(f"Generation {generation}: Best Fitness = {best_fitness}")
            self.best = self.population[self.fitness.index(best_fitness)]

        # Plotting the convergence graph
        plt.plot(best_fitness_over_time)
        plt.xlabel('Generation')
        plt.ylabel('Best Fitness')
        plt.title('Convergence of GA')
        plt.show()

    def get_bins(self, solucao):
        bins = []
        bin_atual = Bin(self.bin_size)

        for item_index in solucao:
            item = self.itens[item_index]
            if not bin_atual.adicionar_item(item):
                bins.append(bin_atual)
                bin_atual = Bin(self.bin_size)
                bin_atual.adicionar_item(item)

        if bin_atual.itens:
            bins.append(bin_atual)

        return bins


def create_data(arquivo):
    caminho = f"/workspaces/Heuristicas/Heuristicas/BPP/BPPInstances/E_120_N_40_60/{
        arquivo}"
    with open(caminho, "r") as file:
        lines = file.read().splitlines()

    itens = list(map(int, filter(None, lines)))
    bin_size = itens[1]
    itens = itens[2:]
    data = {
        "weights": itens,
        "bin_capacity": bin_size,
    }
    return data


data = create_data("E_120_N_40_60_BF0000.bpp")

start_time = time.time()
gga = GGA(data, population_size=100, generations=200, mutation_rate=0.1)
gga.run()
end_time = time.time()
solution = gga.best
bins = gga.get_bins(solution)
print(f"Tempo de execução: {end_time - start_time} segundos")
print("Best solution:", solution)
print("Número de bins usados:", len(bins))
print("Alocação dos itens nos bins (pesos):", [
      [item.peso for item in bin.itens] for bin in bins])
