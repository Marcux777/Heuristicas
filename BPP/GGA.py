import random
from Container import Container


class GGA:
    def __init__(self, 
                 elements, 
                 container_capacity, 
                 num_generations=100, 
                 population_size=20, 
                 stagnation_limit=50, 
                 tournament_size=3):
        
        self.elements = elements
        self.container_capacity = container_capacity
        self.num_generations = num_generations
        self.population_size = population_size
        self.stagnation_limit = stagnation_limit
        self.population = []
        self.tournament_size = tournament_size

    # Gera uma solução inicial
    def generate_initial_solution(self):
        containers = []
        for element in self.elements:
            # Tenta adicionar o elemento a um contêiner existente
            placed = False
            for container in containers:
                if container.remaining_space() >= element:
                    container.add_element(element)
                    placed = True
                    break

            # Se não foi possível colocar o elemento em nenhum contêiner, cria um novo
            if not placed:
                new_container = Container(self.container_capacity)
                new_container.add_element(element)
                containers.append(new_container)

        return containers

    def fitness(self, solution):
        return len(solution)

    # Seleção por torneio
    def tournament_selection(self, population, fitnesses, tournament_size):
        selected = random.sample(
            list(zip(population, fitnesses)), tournament_size)
        selected.sort(key=lambda x: x[1], reverse=True)
        return selected[0][0]

    # Função de cruzamento
    def crossover(self, parent1, parent2):
        # Mistura os contêineres dos dois pais
        all_containers = parent1 + parent2
        random.shuffle(all_containers)

        # Gera dois filhos tentando redistribuir os elementos entre os contêineres
        child1 = self.pack_elements(
            [element for container in parent1 for element in container.elements])
        child2 = self.pack_elements(
            [element for container in parent2 for element in container.elements])

        return child1, child2

    # Função de mutação (muda um elemento de um contêiner para outro)
    def mutate(self, solution):
        if len(solution) > 1:
            container1, container2 = random.sample(solution, 2)
            if container1.elements:
                element = random.choice(container1.elements)
                if container2.remaining_space() >= element:
                    container1.remove_element(element)
                    container2.add_element(element)

        # Remove contêineres vazios
        solution = [container for container in solution if container.elements]
        return solution

    # Função auxiliar para redistribuir os elementos em contêineres
    def pack_elements(self, elements):
        containers = []
        for element in elements:
            placed = False
            for container in containers:
                if container.remaining_space() >= element:
                    container.add_element(element)
                    placed = True
                    break
            if not placed:
                new_container = Container(self.container_capacity)
                new_container.add_element(element)
                containers.append(new_container)
        return containers

    # Função principal que executa o algoritmo genético
    def run(self):
        self.population = [self.generate_initial_solution()
                           for _ in range(self.population_size)]
        best_fitness = -float('inf')
        stagnation_counter = 0

        for generation in range(self.num_generations):
            fitnesses = [self.fitness(individual)
                         for individual in self.population]
            current_best_fitness = max(fitnesses)

            if current_best_fitness > best_fitness:
                best_fitness = current_best_fitness
                stagnation_counter = 0
            else:
                stagnation_counter += 1

            if stagnation_counter >= self.stagnation_limit:
                print(f"Estagnação atingida na geração {
                      generation}. Finalizando o algoritmo.")
                break

            new_population = []
            for _ in range(self.population_size // 2):
                parent1 = self.tournament_selection(self.population, fitnesses, tournament_size=self.tournament_size)
                parent2 = self.tournament_selection(self.population, fitnesses, tournament_size=self.tournament_size)

                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)

                new_population.append(child1)
                new_population.append(child2)

            self.population = new_population

        # Avaliar a última geração e retornar a melhor solução
        best_solution = max(self.population, key=self.fitness)
        print(f"Melhor fitness obtido: {best_fitness}")
        return best_solution


def create_data(Arquivo):
    caminho = f"/workspaces/Heuristicas/Heuristicas/BPP/BPPInstances/E_120_N_40_60/{
        Arquivo}"

    def read_instance(arquivo):
        with open(arquivo, "r") as file:
            lines = file.read()

        return lines

    itens = list(map(int, filter(None, read_instance(caminho).split("\n"))))
    print(itens)
    tam, bin_size = itens[0], itens[1]
    itens.pop(0), itens.pop(0)
    data = {
        "weights": itens,
        "items": list(range(len(itens))),
        "bins": list(range(len(itens))),
        "bin_capacity": bin_size,
    }
    return data


data = create_data("E_120_N_40_60_BF0000.bpp")

gga = GGA(data['weights'], data['bin_capacity'])
best_solution = gga.run()

print("Melhor solução encontrada:")
for container in best_solution:
    print(container)
