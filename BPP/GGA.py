import random
from Container import Container


class GGA:
    def __init__(self, elements):
        """
        Initializes the genetic algorithm parameters for the bin packing problem.

        Args:
            elements (dict): A dictionary containing the following keys:
                - 'weights' (list): A list of item weights.
                - 'bin_capacity' (int): The capacity of each bin.
                - 'num_generations' (int): The number of generations to run the algorithm. Default is 100.
                - 'population_size' (int): The size of the population. Default is 20.
                - 'stagnation_limit' (int): The number of generations with no improvement before stopping. Default is 50.
                - 'tournament_size' (int): The number of individuals to participate in tournament selection. Default is 3.
        """
        self.elements = elements.get('weights', [])
        self.container_capacity = elements.get('bin_capacity', 0)
        self.num_generations = elements.get('num_generations', 100)
        self.population_size = elements.get('population_size', 20)
        self.stagnation_limit = elements.get('stagnation_limit', 50)
        self.tournament_size = elements.get('tournament_size', 3)

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
        original_elements = self.elements
        self.elements = elements
        containers = self.generate_initial_solution()
        self.elements = original_elements
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
                parent1 = self.tournament_selection(
                    self.population, fitnesses, tournament_size=self.tournament_size)
                parent2 = self.tournament_selection(
                    self.population, fitnesses, tournament_size=self.tournament_size)

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
