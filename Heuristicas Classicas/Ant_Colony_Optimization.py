import numpy as np
import math
from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import ParameterSampler
import numpy as np
import heapq

class ACO:
    """
    Classe generalizada ACO - Otimização Colônia de Formigas

    Esta classe implementa o algoritmo ACO (Ant Colony Optimization) para resolver problemas de otimização combinatória.

    Atributos:
        graph (list): Matriz de adjacência do grafo que representa o problema.
        num_ants (int): Número de formigas utilizadas na simulação.
        alpha (float): Fator de influência do feromônio na escolha da próxima cidade.
        beta (float): Fator de influência da distância na escolha da próxima cidade.
        rho (float): Fator de evaporação do feromônio.
        pheromones (list): Matriz de feromônios, onde cada elemento representa a quantidade de feromônio entre duas cidades.

    Métodos:
        construct_solution(start_city) -> list:
            Constrói uma solução (caminho) a partir da cidade inicial.
        select_next_neighbor(current_city, visited_cities) -> int:
            Seleciona a próxima cidade a ser visitada com base na heurística do vizinho mais próximo.    
        select_next_city(current_city, visited_cities) -> int:
            Seleciona a próxima cidade a ser visitada com base nas probabilidades calculadas.
        update_pheromones(solutions) -> None:
            Atualiza os níveis de feromônio com base nas soluções encontradas.
        update_pheromones_Elitist(solutions, elitismo=0.1, Q=1.0) -> None:
            Atualiza os níveis de feromônio no grafo usando a estratégia de otimização elitista de colônia de formigas.
        solve(start_city, max_iterations) -> tuple:
            Resolve o problema de otimização combinatória e retorna a melhor solução e seu custo.
        calculate_cost(solution) -> float:
            Calcula o custo de uma determinada solução.
        find_hyperparameters(graph, start_city, max_iterations, n_iter) -> dict:
            Encontra os melhores hiperparâmetros para o algoritmo ACO.
        two_opt(solution) -> list:
            Aplica a heurística 2-opt para melhorar uma solução.
        lin_kernighan(solution, graph) -> list:
            Aplica a heurística Lin-Kernighan para melhorar uma solução.
        
    """

    def __init__(self, graph, num_ants, alpha, beta, rho):
            """
            Inicializa uma instância da classe AntColonyOptimization.

            Args:
                graph (list): O grafo representado como uma matriz de adjacência.
                num_ants (int): O número de formigas a serem utilizadas na otimização.
                alpha (float): O peso do feromônio na escolha do próximo vértice.
                beta (float): O peso da heurística na escolha do próximo vértice.
                rho (float): Taxa de evaporação do feromônio.

            Attributes:
                graph (list): O grafo representado como uma matriz de adjacência.
                num_ants (int): O número de formigas a serem utilizadas na otimização.
                alpha (float): O peso do feromônio na escolha do próximo vértice.
                beta (float): O peso da heurística na escolha do próximo vértice.
                rho (float): Taxa de evaporação do feromônio.
                pheromones (list): Matriz de feromônios.
                best_solution (None): A melhor solução encontrada até o momento.
            """
            self.graph = np.array(graph)
            self.num_ants = num_ants
            self.alpha = alpha
            self.beta = beta
            self.rho = rho
            self.pheromones = np.ones_like(self.graph)
            self.best_solution = None

    def construct_solution(self, start_city):
        """
        Constrói uma solução (caminho) a partir da cidade inicial.

        Args:
            start_city (int): Índice da cidade inicial.

        Returns:
            list: Lista de cidades que compõem a solução.
        """

        solution = [start_city]
        visited_cities = {start_city}
        current_city = start_city
        num_cities = len(self.graph)

        while len(solution) < num_cities:
            next_city = self.select_next_neighbor(current_city, visited_cities)
            solution.append(next_city)
            visited_cities.add(next_city)
            current_city = next_city

        return solution
    
    def select_next_neighbor(self, current_city, visited_cities):
        """
        Seleciona a próxima cidade a ser visitada com base na heurística do vizinho mais próximo.

        Args:
            current_city (int): Índice da cidade atual.
            visited_cities (list): Lista de cidades já visitadas.

        Returns:
            int: Índice da próxima cidade a ser visitada.
        """

        min_distance = float('inf')
        next_city = None

        for city, distance in enumerate(self.graph[current_city]):
            if city not in visited_cities and distance < min_distance:
                min_distance = distance
                next_city = city

        return next_city
    

    def select_next_city(self, current_city, visited_cities):
        """
        Seleciona a próxima cidade a ser visitada com base nas probabilidades calculadas.

        Args:
            current_city (int): O índice da cidade atual.
            visited_cities (list): Uma lista de índices das cidades já visitadas.

        Returns:
            int: O índice da próxima cidade a ser visitada.
        """
        unvisited_cities = np.array([city for city in range(len(self.graph)) if city not in visited_cities])

        pheromones = self.pheromones[current_city, unvisited_cities]
        distances = self.graph[current_city, unvisited_cities]
        probabilities = pheromones ** self.alpha * (1 / distances) ** self.beta

        probabilities /= np.sum(probabilities)

        next_city = np.random.choice(unvisited_cities, p=probabilities)

        return next_city

    def update_pheromones(self, solutions):
        """
        Atualiza os níveis de feromônio com base nas soluções encontradas.

        Args:
            solutions (list): Lista de soluções (caminhos) encontradas.
        """

        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                self.pheromones[i][j] *= self.rho

        if self.best_solution is not None:
            for i in range(len(self.best_solution) - 1):
                city1 = int(self.best_solution[i])
                city2 = int(self.best_solution[i + 1])
                if(self.graph[city1][city2] != 0):
                    self.pheromones[city1][city2] += (1 / self.graph[city1][city2])
                
    def update_pheromones_Elitist(self, solutions, elitismo=0.1, Q=1.0):
        """
        Atualiza os níveis de feromônio no grafo usando a estratégia de otimização elitista de colônia de formigas.

        Parâmetros:
        - solutions (list): Uma lista de tuplas contendo as soluções encontradas pelas formigas e seus respectivos custos.
        - elitismo (float): O fator de elitismo, representando a proporção de feromônio a ser depositado pela melhor solução.
        - Q (float): A constante de depósito de feromônio.

        Retorna:
        None
        """
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                self.pheromones[i][j] *= self.rho

        best_cost = None
        best_index = None
        if self.best_solution is not None:
            best_cost = self.calculate_cost(self.best_solution)
            best_index = solutions.index((best_cost, self.best_solution))

        for idx, (solution, cost) in enumerate(solutions):
            for i in range(len(solution) - 1):
                city1, city2 = solution[i], solution[i + 1]
                delta_pheromone = Q / cost  # Feromônio depositado por cada formiga
                self.pheromones[city1][city2] += delta_pheromone

                if idx == best_index:
                    delta_pheromone_best = Q / best_cost  # Feromônio depositado pela melhor solução
                    self.pheromones[city1][city2] += elitismo * delta_pheromone_best


    def solve(self, start_city, max_iterations):
        """
        Resolve o problema de otimização combinatória e retorna a melhor solução e seu custo.

        Args:
            start_city (int): Índice da cidade inicial.
            max_iterations (int): Número máximo de iterações.

        Returns:
            tuple: Tupla contendo a melhor solução e seu custo.
        """

        self.best_solution = None
        best_cost = float('inf')

        for _ in range(max_iterations):
            solutions = []
            for _ in range(self.num_ants):
                solution = self.construct_solution(start_city)
                heapq.heappush(solutions, (self.calculate_cost(solution), solution))

            current_best_cost, current_best_solution = heapq.heappop(solutions)
            if self.best_solution is None or current_best_cost < best_cost:
                self.best_solution = current_best_solution
                best_cost = current_best_cost

            self.update_pheromones(solutions)

        self.best_solution = self.two_opt(self.best_solution)
        #self.best_solution = self.lin_kernighan(self.best_solution)
        best_cost = self.calculate_cost(self.best_solution)

        return self.best_solution, best_cost


    def calculate_cost(self, solution):
        """
        Calcula o custo de uma determinada solução.

        Args:
            solution (list): Lista de cidades que compõem a solução.

        Returns:
            float: Custo da solução.
        """

        cost = 0
        for i in range(len(solution) - 1):
            cost += self.graph[solution[i]][solution[i + 1]]
        return cost

    @staticmethod
    def find_hyperparameters(graph, start_city, max_iterations, n_iter):
        """
        Encontra os melhores hiperparâmetros para o algoritmo de otimização por colônia de formigas.

        Args:
            graph (Graph): O grafo representando as cidades e as distâncias entre elas.
            start_city (int): O índice da cidade de partida.
            max_iterations (int): O número máximo de iterações para executar o algoritmo.
            n_iter (int): O número de combinações de hiperparâmetros a serem testadas.

        Returns:
            dict: Um dicionário contendo os melhores hiperparâmetros encontrados.

        """
        param_grid = {
            'num_ants': [50, 100],
            'alpha': np.linspace(0.1, 1.0, 10),
            'beta': np.linspace(0.1, 1.0, 10),
            'rho': np.linspace(0.1, 1.0, 10)
        }

        param_list = list(ParameterSampler(param_grid, n_iter))

        best_cost = float('inf')
        best_params = None

        for params in param_list:
            aco = ACO(graph, **params)
            _, cost = aco.solve(start_city, max_iterations)
            
            if cost < best_cost:
                best_cost = cost
                best_params = params
                
            print(best_params)

        return best_params
    
    def two_opt(self, solution):
        """
        Aplica a heurística 2-opt para melhorar uma solução.

        Args:
            solution (list): Lista de cidades que compõem a solução.

        Returns:
            list: Nova solução após a aplicação da heurística 2-opt.
        """
        best_solution = solution
        improved = True
        while improved:
            improved = False
            for i in range(1, len(solution) - 2):
                for j in range(i + 1, len(solution)):
                    if j - i == 1: continue 
                    new_solution = solution[:i] + solution[i:j][::-1] + solution[j:]
                    old_cost = self.calculate_cost(solution[i-1:i+1]) + self.calculate_cost(solution[j-1:j+1])
                    new_cost = self.calculate_cost(new_solution[i-1:i+1]) + self.calculate_cost(new_solution[j-1:j+1])
                    if new_cost < old_cost:
                        solution = new_solution
                        improved = True
        return solution
    