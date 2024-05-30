# Classe generalizada ACO - Otimização Colônia de Formigas

import numpy as np
import math

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
            solution.append(next_city)
            visited_cities.append(next_city)
            current_city = next_city

        return solution

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

        # Verifique se há alguma probabilidade
        if len(probabilities) > 0:
            # Normalize as probabilidades se necessário
            probabilities = np.array(probabilities) / np.sum(probabilities)
            return np.random.choice(unvisited_cities, p=probabilities)
        else:
            # Se todas as cidades foram visitadas, retorne a cidade inicial
            return current_city

    def update_pheromones(self, solutions):
        """
        Atualiza os níveis de feromônio com base nas soluções encontradas.

        Args:
            solutions (list): Lista de soluções (caminhos) encontradas.
        """

        for solution, cost in solutions:
            for i in range(len(solution) - 1):
                # Converta os valores de solution[i] e solution[i + 1] para inteiros
                city1 = int(solution[i])
                city2 = int(solution[i + 1])
                self.pheromones[city1][city2] += 1 / self.graph[city1][city2]

        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                self.pheromones[i][j] *= self.rho

    def solve(self, start_city, max_iterations):
        """
        Resolve o problema de otimização combinatória e retorna a melhor solução e seu custo.

        Args:
            start_city (int): Índice da cidade inicial.
            max_iterations (int): Número máximo de iterações.

        Returns:
            tuple: Tupla contendo a melhor solução e seu custo.
        """

        best_solution = None
        best_cost = float('inf')

        for _ in range(max_iterations):
            solutions = []
            for _ in range(self.num_ants):
                solution = self.construct_solution(start_city)
                cost = self.calculate_cost(solution)
                solutions.append((solution, cost))

            self.update_pheromones(solutions)

            best_solution, best_cost = min(solutions, key=lambda x: x[1])

        return best_solution, best_cost

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
