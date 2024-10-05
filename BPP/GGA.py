import random
from Container import Container


""" Todo
- Controle de Diversidade (Diversificação)
- Elitismo
"""


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
                - 'mutation_rate' (float): The probability of mutation. Default is 0.1.
                - 'elite_rating' (float): The percentage of the population to be considered elite. Default is 0.1.
        """
        self.elements = elements.get('weights', [])
        self.container_capacity = elements.get('bin_capacity', 0)
        self.num_generations = elements.get('num_generations', 100)
        self.population_size = elements.get('population_size', 20)
        self.stagnation_limit = elements.get('stagnation_limit', 50)
        self.tournament_size = elements.get('tournament_size', 3)
        self.mutation_rate = elements.get('mutation_rate', 0.1)
        self.elite_rating = elements.get('elite_rating', 0.1)

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
        """
            penalizar soluções onde os contêineres não estão bem preenchidos. 
            Ajustando a função de fitness para considerar o espaço desperdiçado 
            em cada contêiner
        """
        total_waste = sum(container.remaining_space()
                          for container in solution)
        return len(solution) + (total_waste / self.container_capacity)

    # Seleção por torneio

    def tournament_selection(self, population, fitnesses, tournament_size):
        selected = random.sample(
            list(zip(population, fitnesses)), tournament_size)
        selected.sort(key=lambda x: x[1], reverse=True)
        return selected[0][0]

    def stoic_tournament_selection(self, population, fitnesses, tournament_size):
        selected = random.sample(
            list(zip(population, fitnesses)), tournament_size)
        selected.sort(key=lambda x: x[1], reverse=True)

        # Probabilidade de selecionar o melhor, mas com chance de selecionar outro
        if random.random() < 0.75:  # 75% de chance de selecionar o melhor
            return selected[0][0]
        else:
            return random.choice(selected)[0]

    # Função de cruzamento divisão unica
    def crossover(self, parent1, parent2):
        """
        Perform crossover operation between two parent solutions to generate two offspring.

        This method takes two parent solutions, extracts their elements, and combines them
        to create two new offspring solutions. The elements from the parents are split at
        the midpoint and recombined to form the offspring.

        Args:
            parent1 (list): The first parent solution, where each element is a container with elements.
            parent2 (list): The second parent solution, where each element is a container with elements.

        Returns:
            tuple: A tuple containing two offspring solutions, each represented as a list of containers.
        """
        # Coleta todos os elementos dos dois pais
        elements1 = [
            element for container in parent1 for element in container.elements]
        elements2 = [
            element for container in parent2 for element in container.elements]

        # Divide os elementos em dois grupos para criar dois filhos
        midpoint = len(elements1) // 2
        child1_elements = elements1[:midpoint] + elements2[midpoint:]
        child2_elements = elements2[:midpoint] + elements1[midpoint:]

        # Gera dois filhos redistribuindo os elementos entre os contêineres
        child1 = self.pack_elements(child1_elements)
        child2 = self.pack_elements(child2_elements)

        return child1, child2

    # Função de cruzamento divisão Multi-Pontos
    def crossover_multipoint(self, parent1, parent2):
        elements1 = [
            element for conteiner in parent1 for element in conteiner.elements]
        elements2 = [
            element for conteiner in parent2 for element in conteiner.elements]

        point1 = random.randint(1, len(elements1) - 2)
        point2 = random.randint(point1 + 1, len(elements1) - 1)

        child1_elements = elements1[:point1] + \
            elements2[point1:point2] + elements1[point2:]
        child2_elements = elements2[:point1] + \
            elements1[point1:point2] + elements2[point2:]

        child1 = self.pack_elements(child1_elements)
        child2 = self.pack_elements(child2_elements)

        return child1, child2

    # Função de mutação (muda um elemento de um contêiner para outro)
    def mutate(self, solution, mutation_rate):
        if random.random() < mutation_rate:
            self._mutate_solution(solution)
            solution = self._remove_empty_containers(solution)
        return solution

    def _mutate_solution(self, solution):
        if len(solution) > 1:
            container1, container2 = random.sample(solution, 2)
            if container1.elements:
                element = random.choice(container1.elements)
                if container2.remaining_space() >= element:
                    container1.remove_element(element)
                    container2.add_element(element)

    def _remove_empty_containers(self, solution):
        return [container for container in solution if container.elements]

    # Função auxiliar para redistribuir os elementos em contêineres
    def pack_elements(self, elements):
        original_elements = self.elements
        self.elements = elements
        containers = self.generate_initial_solution()
        self.elements = original_elements
        return containers

    # Função principal que executa o algoritmo genético
    def run(self):
        self.initialize_population()
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
                print(
                    f"Estagnação atingida na geração {generation}. Finalizando o algoritmo...")
                break

            self.population = self.create_new_population(fitnesses)

        best_solution = max(self.population, key=self.fitness)
        print(f"Melhor fitness obtido: {best_fitness}")
        return best_solution

    def initialize_population(self):
        self.population = [self.generate_initial_solution()
                           for _ in range(self.population_size)]

    def create_new_population(self, fitnesses):
        # aplicação do elitismo
        elite_size = int(self.elite_rating * self.population_size)
        elite = sorted(self.population, key=self.fitness)[:elite_size]
        new_population = elite.copy()  # Garantir que a elite passe para a próxima geração

        while len(new_population) < self.population_size:
            parent1 = self.stoic_tournament_selection(
                self.population, fitnesses, tournament_size=self.tournament_size)
            parent2 = self.stoic_tournament_selection(
                self.population, fitnesses, tournament_size=self.tournament_size)

            child1, child2 = self.crossover_multipoint(parent1, parent2)
            child1 = self.mutate(child1, self.mutation_rate)
            child2 = self.mutate(child2, self.mutation_rate)

            new_population.append(child1)
            if len(new_population) < self.population_size:
                new_population.append(child2)

        return new_population
