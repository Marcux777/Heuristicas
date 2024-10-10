import random
from copy import deepcopy
from Container import Container
from Tabu_Search import Tabu_Search
import optuna
import numpy as np


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
                - 'tabu_max_iterations' (int): Maximum number of iterations for Tabu Search. Default is 30.
                - 'tabu_tenure' (int): Number of iterations a move remains in the tabu list. Default is 5.
                - 'tabu_max_neighbors' (int): Maximum number of neighbors to consider in each iteration. Default is 20.
        """
        self.elements = elements.get('weights', [])
        self.container_capacity = elements.get('bin_capacity', 0)
        self.num_generations = elements.get('num_generations', 165)
        self.population_size = elements.get('population_size', 65)
        self.stagnation_limit = elements.get('stagnation_limit', 50)
        self.tournament_size = elements.get('tournament_size', 3)
        self.mutation_rate = elements.get('mutation_rate', 0.2683891676635783)
        self.elite_rating = elements.get('elite_rating', 0.10116734035019169)

        # Parâmetros da Tabu Search
        self.tabu_max_iterations = elements.get('tabu_max_iterations', 30)
        self.tabu_tenure = elements.get('tabu_tenure', 20)
        self.tabu_max_neighbors = elements.get('tabu_max_neighbors', 29)

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

# -------------------------------- Metodos de Seleção -------------------------------- #

    # Seleção por torneio

    def tournament_selection(self, population, fitnesses, tournament_size):
        selected = random.sample(
            list(zip(population, fitnesses)), tournament_size)
        selected.sort(key=lambda x: x[1], reverse=True)
        return selected[0][0]

    def stoic_tournament_selection(self, population, fitnesses, tournament_size):
        selected = random.sample(
            list(zip(population, fitnesses)), tournament_size)
        # Seleciona o melhor indivíduo sem ordenar a lista inteira
        best_individual = max(selected, key=lambda x: x[1])
        if random.random() < 0.75:
            return best_individual[0]
        else:
            return random.choice(selected)[0]

    def roulette_wheel_selection(self, population, fitnesses):

        # Inverter os valores de fitness se menor fitness for melhor
        # Neste caso, parece que um valor de fitness menor é melhor
        max_fitness = max(fitnesses)
        adjusted_fitnesses = [max_fitness - f +
                              1 for f in fitnesses]  # +1 para evitar zero

        total_fitness = sum(adjusted_fitnesses)
        probabilities = [f / total_fitness for f in adjusted_fitnesses]

        # Gerar um número aleatório entre 0 e 1
        r = random.random()
        cumulative_probability = 0.0

        for individual, probability in zip(population, probabilities):
            cumulative_probability += probability
            if cumulative_probability >= r:
                return individual

        # Retorna o último indivíduo se nenhuma seleção for feita
        return population[-1]

# -------------------------------- Metodos de Cruzamento -------------------------------- #

    # Função de cruzamento divisão unica

    def single_point_crossover(self, parent1, parent2):
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
    def multi_point_crossover(self, parent1, parent2):
        elements1 = [
            element for conteiner in parent1 for element in conteiner.elements]
        elements2 = [
            element for conteiner in parent2 for element in conteiner.elements]

        if len(elements1) < 2:
            return parent1, parent2  # Não há pontos suficientes para cruzamento

        point1 = random.randint(1, len(elements1) - 2)
        point2 = random.randint(point1 + 1, len(elements1) - 1)

        child1_elements = elements1[:point1] + \
            elements2[point1:point2] + elements1[point2:]
        child2_elements = elements2[:point1] + \
            elements1[point1:point2] + elements2[point2:]

        child1 = self.pack_elements(child1_elements)
        child2 = self.pack_elements(child2_elements)

        return child1, child2

    def pmx_crossover(self, parent1, parent2):
        """
        Implementa o cruzamento PMX (Partially Matched Crossover) adaptado para o GGA.
        Realiza o cruzamento entre dois pais e garante que os itens não sejam duplicados nos filhos.
        """

        # Coleta todos os itens dos dois pais
        elements1 = [
            element for container in parent1 for element in container.elements]
        elements2 = [
            element for container in parent2 for element in container.elements]

        # Verifica se ambos os pais têm o mesmo número de elementos
        if len(elements1) != len(elements2):
            raise ValueError(
                "Os pais devem conter o mesmo número de elementos.")

        # Escolhe dois pontos de cruzamento
        point1, point2 = sorted(random.sample(range(len(elements1)), 2))

        # Inicializa os filhos como cópias dos pais
        child1_elements = elements1[:]
        child2_elements = elements2[:]

        # Troca os segmentos entre os dois pais
        child1_elements[point1:point2], child2_elements[point1:
                                                        point2] = elements2[point1:point2], elements1[point1:point2]

        # Mapeamento das trocas entre as subsequências para ambos os filhos
        mapping_1_to_2 = {elements1[i]: elements2[i]
                          for i in range(point1, point2)}
        mapping_2_to_1 = {elements2[i]: elements1[i]
                          for i in range(point1, point2)}

        # Corrige as colisões em ambos os filhos com os mapeamentos
        self._pmx_fix_collisions(
            child1_elements, mapping_1_to_2, point1, point2)
        self._pmx_fix_collisions(
            child2_elements, mapping_2_to_1, point1, point2)

        # Reorganiza os itens para criar os filhos a partir dos elementos ajustados
        child1 = self.pack_elements(child1_elements)
        child2 = self.pack_elements(child2_elements)

        return child1, child2

    def uniform_crossover(self, parent1, parent2):
        return None

    def arithmetic_Crossover(self, parent1, parent2):
        return None

    def order_Crossover(self, parent1, parent2):
        return None

    def cicly_Crossover(self, parent1, parent2):
        return None
# -------------------------------- Metodo de Mutações -------------------------------- #

    # Função de mutação
    def mutate(self, solution, mutation_rate):
        if random.random() < mutation_rate:
            self._inversion_Mutation(solution)
            solution = self._remove_empty_containers(solution)
        return solution

    # Funções para as Mutações
    def _swap_Mutation(self, solution):
        """
        Realiza a mutação de troca entre dois elementos de contêineres diferentes.

        Args:
            solution (list): Lista de contêineres representando a solução atual.

        Returns:
            list: Solução mutada com dois elementos trocados entre contêineres.
        """
        # Cria uma cópia profunda da solução para evitar modificações in-place
        mutated_solution = [container.copy() for container in solution]

        # Filtra os contêineres que possuem pelo menos um elemento
        eligible_containers = [c for c in mutated_solution if c.elements]
        if len(eligible_containers) < 2:
            # Não há contêineres suficientes para realizar uma troca
            return mutated_solution

        # Seleciona aleatoriamente dois contêineres distintos
        container1, container2 = random.sample(eligible_containers, 2)

        # Seleciona um elemento aleatório de cada contêiner
        element1 = random.choice(container1.elements)
        element2 = random.choice(container2.elements)

        # Verifica se a troca é viável para ambos os contêineres
        can_swap = (
            container1.remaining_space() + element1 - element2 >= 0 and
            container2.remaining_space() + element2 - element1 >= 0
        )

        if can_swap:
            # Realiza a troca de elementos entre os contêineres
            container1.remove_element(element1)
            container2.remove_element(element2)
            container1.add_element(element2)
            container2.add_element(element1)
            # Atualiza o espaço utilizado nos contêineres
            container1.used = sum(container1.elements)
            container2.used = sum(container2.elements)

        return mutated_solution

    def _inversion_Mutation(self, solution):
        """
        Realiza a mutação de inversão em uma solução.

        Args:
            solution (list): Lista de contêineres representando a solução atual.

        Returns:
            list: Solução mutada com uma subsequência de itens invertida em um contêiner.
        """
        # Cria uma cópia superficial dos contêineres com cópias internas
        mutated_solution = [container.copy() for container in solution]

        # Filtra contêineres que possuem pelo menos dois itens
        eligible_containers = [
            c for c in mutated_solution if len(c.elements) >= 2]
        if not eligible_containers:
            # Não há contêineres elegíveis para mutação de inversão
            return mutated_solution

        # Seleciona aleatoriamente um contêiner elegível
        container = random.choice(eligible_containers)

        # Seleciona dois índices para definir a subsequência a ser invertida
        idx1, idx2 = sorted(random.sample(range(len(container.elements)), 2))

        # Inverte a subsequência de itens entre idx1 e idx2
        container.elements[idx1:idx2] = container.elements[idx1:idx2][::-1]

        # Atualiza o espaço usado no contêiner
        container.used = sum(container.elements)

        return mutated_solution

    def _insertion_Mutation(self, solution):
        """
        Perform an insertion mutation on the given solution.

        This method creates a deep copy of the provided solution to avoid in-place modifications.
        It randomly selects two different containers from the solution. If the first container
        has elements, it randomly selects an element from it, removes the element, and attempts
        to insert it into the second container. If the second container does not have enough space
        for the element, a new container is created and the element is added to it.

        Args:
            solution (list): A list of containers representing the current solution.

        Returns:
            list: A new list of containers representing the mutated solution.
        """
        # Cria uma cópia profunda da solução para evitar modificações in-place
        mutated_solution = [container.copy() for container in solution]

        # Seleciona aleatoriamente dois contêineres diferentes
        container1, container2 = random.sample(mutated_solution, 2)

        if container1.elements:
            # Seleciona um item aleatório do container1
            element = random.choice(container1.elements)
            container1.remove_element(element)

            # Se possível, tenta inserir o item em container2
            if container2.remaining_space() >= element:
                container2.add_element(element)
            else:
                # Se container2 não tiver espaço, crie um novo contêiner
                new_container = Container(self.container_capacity)
                new_container.add_element(element)
                mutated_solution.append(new_container)

        return mutated_solution

    def _scramble_Mutation(self, solution):
        """
        Perform a scramble mutation on a given solution.

        This mutation selects a random container with at least two elements,
        chooses a subsequence within that container, and shuffles the elements
        in that subsequence.

        Args:
            solution (list): A list of containers, where each container is an
                             object with an 'elements' attribute (a list of elements)
                             and a 'used' attribute (an integer representing the used space).

        Returns:
            list: A new solution with the mutated container.
        """
        mutated_solution = [container.copy() for container in solution]

        # Filtra os contêineres com pelo menos dois elementos
        eligible_containers = [
            c for c in mutated_solution if len(c.elements) > 1]
        if not eligible_containers:
            return mutated_solution

        # Seleciona um contêiner aleatório
        container = random.choice(eligible_containers)

        # Seleciona dois índices e embaralha os elementos nessa subsequência
        idx1, idx2 = sorted(random.sample(range(len(container.elements)), 2))
        subsequence = container.elements[idx1:idx2]
        random.shuffle(subsequence)
        container.elements[idx1:idx2] = subsequence

        # Atualiza o espaço usado no contêiner
        container.used = sum(container.elements)

        return mutated_solution

    def _gausian_Mutation(self, solution):
        """
        Applies a Gaussian mutation to a given solution.

        This method selects a random container and a random item within that container,
        then applies a Gaussian mutation to the item's weight, simulating small variations.
        The mutated weight is checked to ensure it fits within the container's remaining space.

        Parameters:
        solution (list): A list of containers, where each container has a list of elements (weights).

        Returns:
        list: A new solution with the mutated item weight.
        """
        mutated_solution = [container.copy() for container in solution]

        # Seleciona aleatoriamente um contêiner e um item dentro desse contêiner
        eligible_containers = [c for c in mutated_solution if c.elements]
        if not eligible_containers:
            return mutated_solution

        container = random.choice(eligible_containers)
        element_idx = random.randint(0, len(container.elements) - 1)

        # Aplica uma mutação gaussiana ao item (simulando pequenas variações no peso)
        original_weight = container.elements[element_idx]
        mutated_weight = abs(np.random.normal(
            loc=original_weight, scale=original_weight * 0.1))  # Variação de 10%

        # Verifica se o novo peso cabe no contêiner
        if container.remaining_space() + container.elements[element_idx] >= mutated_weight:
            container.elements[element_idx] = mutated_weight
            # Atualiza o espaço utilizado
            container.used = sum(container.elements)

        return mutated_solution

    def _bitflip_Mutation(self, solution):
        """
        Perform a bit-flip mutation on the given solution.

        This mutation selects two different containers from the solution and attempts to move a random element
        from the first container to the second container. If the second container does not have enough space
        for the element, a new container is created and the element is added to it.

        Args:
            solution (list): A list of containers representing the current solution.

        Returns:
            list: A new solution with the mutation applied.
        """
        mutated_solution = [container.copy() for container in solution]

        # Seleciona aleatoriamente dois contêineres diferentes
        container1, container2 = random.sample(mutated_solution, 2)

        if container1.elements:
            # Seleciona um item aleatório do container1
            element = random.choice(container1.elements)
            container1.remove_element(element)

            # Se possível, tenta inserir o item em container2
            if container2.remaining_space() >= element:
                container2.add_element(element)
            else:
                # Se container2 não tiver espaço, crie um novo contêiner
                new_container = Container(self.container_capacity)
                new_container.add_element(element)
                mutated_solution.append(new_container)

        return mutated_solution

# -------------------------------- Metodos Auxiliares -------------------------------- #

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

        TS = Tabu_Search(self, max_iterations=self.tabu_max_iterations,
                         tabu_tenure=self.tabu_tenure, max_neighbors=self.tabu_max_neighbors)
        improved_elite = []
        for individual in elite:
            improved_individual = TS.search(individual)
            improved_elite.append(improved_individual)
        new_population = improved_elite.copy()

        while len(new_population) < self.population_size:
            parent1 = self.roulette_wheel_selection(
                self.population, fitnesses)
            parent2 = self.roulette_wheel_selection(
                self.population, fitnesses)

            child1, child2 = self.multi_point_crossover(parent1, parent2)
            child1 = self.mutate(child1, self.mutation_rate)
            child2 = self.mutate(child2, self.mutation_rate)

            new_population.append(child1)
            if len(new_population) < self.population_size:
                new_population.append(child2)

        return new_population

    def _pmx_fix_collisions(self, child_elements, mapping, point1, point2):
        """
        Corrige colisões causadas pelo cruzamento PMX, garantindo que cada item apareça apenas uma vez.

        Args:
            child_elements (list): Os elementos do filho gerado após a troca.
            parent1_elements (list): Elementos do primeiro pai.
            parent2_elements (list): Elementos do segundo pai.
            point1 (int): Primeiro ponto de cruzamento.
            point2 (int): Segundo ponto de cruzamento.
        """
        swapped_elements = set(child_elements[point1:point2])

        # Percorre os elementos fora da faixa de cruzamento
        for i in list(range(0, point1)) + list(range(point2, len(child_elements))):
            # Se o elemento estiver em swapped_elements, ele precisa ser corrigido
            while child_elements[i] in swapped_elements:
                child_elements[i] = mapping[child_elements[i]]

    # Função para otimização dos hiperparametross
    def call_optuna(self):
        def objective(trial):
            # Hiperparâmetros a serem otimizados
            hyperparameters = {
                'num_generations': trial.suggest_int('num_generations', 50, 200),
                'population_size': trial.suggest_int('population_size', 10, 100),
                'mutation_rate': trial.suggest_float('mutation_rate', 0.01, 0.5),
                'elite_rating': trial.suggest_float('elite_rating', 0.01, 0.5),
                'tabu_max_iterations': trial.suggest_int('tabu_max_iterations', 10, 100),
                'tabu_tenure': trial.suggest_int('tabu_tenure', 1, 20),
                'tabu_max_neighbors': trial.suggest_int('tabu_max_neighbors', 5, 50),
                'weights': [random.randint(1, 100) for _ in range(50)],
                'bin_capacity': 150
            }

            # Inicializar e executar o GGA
            gga = GGA(hyperparameters)

            best_solution = gga.run()
            best_fitness = gga.fitness(best_solution)

            # O Optuna minimiza por padrão, então fitness negativo pode ser necessário se maior for melhor
            return best_fitness

        # Alterar para "maximize" se necessário
        study = optuna.create_study(direction="minimize")
        study.optimize(objective, n_trials=20)

        # Exibir os melhores hiperparâmetros
        print("Melhores hiperparâmetros encontrados:", study.best_params)
        return study.best_params
