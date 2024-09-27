import random
import os
import glob


class GGA:
    def __init__(self, bin_size, population_size, generations, mutation_rate, itens):
        self.bin_size = bin_size
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.itens = itens
        self.itens.sort(reverse=True)
        self.population = self.initialize_population()
        self.fitness = []

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            bins = []
            for item in self.itens:
                placed = False
                for bin in bins:
                    if sum(bin) + item <= self.bin_size:
                        bin.append(item)
                        placed = True
                        break
                if not placed:
                    bins.append([item])
            population.append(bins)
        return population

    def evaluate_fitness(self, bins):
        return len(bins)

    def selection(self):
        tournament_size = 3
        selected = []
        for _ in range(self.population_size):
            tournament = random.sample(self.population, tournament_size)
            tournament_fitness = [self.evaluate_fitness(bins) for bins in tournament]
            selected.append(
                tournament[tournament_fitness.index(min(tournament_fitness))]
            )
        return selected

    def crossover(self, parent1, parent2):
        # Combinar grupos de diferentes soluções
        child1, child2 = [], []
        for bin1, bin2 in zip(parent1, parent2):
            if random.random() > 0.5:
                child1.append(bin1)
                child2.append(bin2)
            else:
                child1.append(bin2)
                child2.append(bin1)
        return child1, child2

    def mutate(self, bins):
        for bin in bins:
            if random.random() < self.mutation_rate:
                item = bin.pop(random.randint(0, len(bin) - 1))
                self.place_item_in_bins(item, bins)
        return bins

    def place_item_in_bins(self, item, bins):
        for bin in bins:
            if sum(bin) + item <= self.bin_size:
                bin.append(item)
                return
        bins.append([item])

    def run(self):
        for generation in range(self.generations):
            self.fitness = [self.evaluate_fitness(bins) for bins in self.population]
            new_population = []
            selected = self.selection()
            for i in range(0, self.population_size, 2):
                parent1, parent2 = selected[i], selected[i + 1]
                child1, child2 = self.crossover(parent1, parent2)
                new_population.append(self.mutate(child1))
                new_population.append(self.mutate(child2))
            self.population = new_population
            best_fitness = min(self.fitness)
            print(f"Generation {generation}: Best Fitness = {best_fitness}")
            self.best = self.population[self.fitness.index(best_fitness)]


caminho = "C:\\Users\\20211002801130\\Documents\\GitHub\\Heuristicas\\BPP\\BPP Instances\\E_120_N_40_60\\E_120_N_40_60_BF0000.bpp"


def read_instance(arquivo):
    with open(arquivo, "r") as file:
        lines = file.read()

    return lines


"""itens = list(map(int, filter(None, read_instance(caminho).split("\n"))))
print(itens)
tam, bin_size = itens[0], itens[1]
itens.pop(0), itens.pop(0)"""

itens = [48, 30, 19, 36, 36, 27, 42, 42, 36, 24, 30]
bin_size = 100

# 30 27 30 = 87
# 48 42 = 90
# 19 36 42 = 97
# 36 36 24 = 96


gga = GGA(
    bin_size=bin_size,
    population_size=100,
    generations=200,
    mutation_rate=0.1,
    itens=itens,
)
gga.run()
print("Best solution:", gga.best)
