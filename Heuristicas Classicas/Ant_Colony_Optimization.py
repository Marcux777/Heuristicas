# Classe generalizada ACO - Otimização Colônia de Formigas

import numpy as np
import math
from sklearn.model_selection import ParameterGrid

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
        select_next_city(current_city, visited_cities) -> int:
            Seleciona a próxima cidade a ser visitada com base nas probabilidades calculadas.
        update_pheromones(solutions) -> None:
            Atualiza os níveis de feromônio com base nas soluções encontradas.
        solve(start_city, max_iterations) -> tuple:
            Resolve o problema de otimização combinatória e retorna a melhor solução e seu custo.
        calculate_cost(solution) -> float:
            Calcula o custo de uma determinada solução.
    """

    def __init__(self, graph, num_ants, alpha, beta, rho):
        self.graph = graph
        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.pheromones = [[1 for _ in range(len(graph))] for _ in range(len(graph))]
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
        visited_cities = [start_city]
        current_city = start_city

        while len(solution) < len(self.graph):
            next_city = self.select_next_city(current_city, visited_cities)
            # next_city = self.select_next_neighbor(current_city, visited_cities)
            solution.append(next_city)
            visited_cities.append(next_city)
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

        unvisited_cities = set(range(len(self.graph))) - set(visited_cities)
        next_city = min(unvisited_cities, key=lambda city: self.graph[current_city][city])
        return next_city

    def select_next_city(self, current_city, visited_cities):
        """
        Seleciona a próxima cidade a ser visitada com base nas probabilidades calculadas.

        Args:
            current_city (int): Índice da cidade atual.
            visited_cities (list): Lista de cidades já visitadas.

        Returns:
            int: Índice da próxima cidade a ser visitada.
        """

        probabilities = []
        unvisited_cities = [city for city in range(len(self.graph)) if city not in visited_cities]
        for next_city in unvisited_cities:
            pheromone = self.pheromones[current_city][next_city]
            distance = self.graph[current_city][next_city]
            probability = pheromone ** self.alpha * (1 / distance) ** self.beta
            probabilities.append(probability)

        if len(probabilities) > 0:
            probabilities = np.array(probabilities) / np.sum(probabilities)
            return np.random.choice(unvisited_cities, p=probabilities)
        else:
            return current_city

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
                self.pheromones[city1][city2] += (1 / self.graph[city1][city2])

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
                cost = self.calculate_cost(solution)
                solutions.append((solution, cost))

            current_best_solution, current_best_cost = min(solutions, key=lambda x: x[1])
            if self.best_solution is None or current_best_cost < best_cost:
                self.best_solution = current_best_solution
                best_cost = current_best_cost

            self.update_pheromones(solutions)

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
    def find_hyperparamenters(graph, start_city, max_iterations):
        # Defina os valores dos hiperparâmetros que você deseja testar
        param_grid = {
            'num_ants': [50, 100],
            'alpha': [0.1, 0.5],
            'beta': [0.1, 0.5],
            'rho': [0.3, 0.5]
        }

        # Crie uma grade de hiperparâmetros
        grid = ParameterGrid(param_grid)

        best_cost = float('inf')
        best_params = None

        # Para cada combinação de hiperparâmetros
        for params in grid:
            # Crie uma instância do ACO com os hiperparâmetros atuais
            aco = ACO(graph, **params)
            print(params)
            # Resolva o problema e obtenha o custo da melhor solução
            _, cost = aco.solve(start_city, max_iterations)

            # Se o custo da melhor solução for menor que o melhor custo encontrado até agora
            if cost < best_cost:
                # Atualize o melhor custo e os melhores hiperparâmetros
                best_cost = cost
                best_params = params

        return best_params
