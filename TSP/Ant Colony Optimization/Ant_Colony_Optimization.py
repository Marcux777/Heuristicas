import numpy as np
import math
from sklearn.model_selection import ParameterGrid, ParameterSampler
import heapq
import random


class ACO:
    def __init__(self, graph, num_ants, alpha=1.0, beta=2.0, rho=0.5, Q=1.0):
        """
        Inicializa uma instância da classe AntColonyOptimization.

        Args:
            graph (list): O grafo representado como uma matriz de adjacência.
            num_ants (int): O número de formigas a serem utilizadas na otimização.
            alpha (float): O peso do feromônio na escolha do próximo vértice.
            beta (float): O peso da heurística na escolha do próximo vértice.
            rho (float): Taxa de evaporação do feromônio.
            Q (float): Quantidade de feromônio depositada pelas formigas.

        Attributes:
            graph (list): O grafo representado como uma matriz de adjacência.
            num_ants (int): O número de formigas a serem utilizadas na otimização.
            alpha (float): O peso do feromônio na escolha do próximo vértice.
            beta (float): O peso da heurística na escolha do próximo vértice.
            rho (float): Taxa de evaporação do feromônio.
            Q (float): Quantidade de feromônio depositada pelas formigas.
            pheromones (list): Matriz de feromônios.
            best_solution (None): A melhor solução encontrada até o momento.
        """
        self.graph = np.array(graph)
        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.pheromones = np.ones_like(self.graph)
        self.best_solution = None
        self.best_cost = float("inf")

    def run(self, start_city, max_iterations):
        for _ in range(max_iterations):
            solutions = [
                self.generate_solutions(start_city) for _ in range(self.num_ants)
            ]
            self.update_pheromones(solutions)
            self.update_best_solution(solutions)

        return [self.best_solution, self.best_cost]

    def generate_solutions(self, start_city):
        num_cities = len(self.graph)
        solution = [start_city]
        visited = np.zeros(num_cities, dtype=bool)
        visited[start_city] = True
        curr = start_city
        while not visited.all():
            next_city = self.probabilistic_choice(visited, curr)
            solution.append(next_city)
            visited[next_city] = True
            curr = next_city

        return solution

    def probabilistic_choice(self, visited, current_city):
        unvisited_cities = np.where(~visited)[0]  # Índices das cidades não visitadas

        pheromones = self.pheromones[current_city, unvisited_cities]
        distances = self.graph[current_city, unvisited_cities]
        probabilities = pheromones**self.alpha * (1 / distances) ** self.beta
        probabilities /= np.sum(probabilities)

        next_city = np.random.choice(unvisited_cities, p=probabilities)
        return next_city

    def update_pheromones(self, solutions):
        self.pheromones *= 1 - self.rho

        costs = [
            self.calculate_cost(sol) for sol in solutions
        ]  # Calcula os custos uma vez

        for sol, cost in zip(solutions, costs):
            from_cities = sol[:-1]  # Todas as cidades, exceto a última
            to_cities = sol[1:]  # Todas as cidades, exceto a primeira

            self.pheromones[from_cities, to_cities] += 1.0 / cost
            self.pheromones[to_cities, from_cities] += 1.0 / cost

        # Elitismo
        if self.best_solution is not None:
            best_cost = self.calculate_cost(self.best_solution)
            from_cities = self.best_solution[:-1]
            to_cities = self.best_solution[1:]
            self.pheromones[from_cities, to_cities] += self.Q / best_cost
            self.pheromones[to_cities, from_cities] += self.Q / best_cost

    def calculate_cost(self, solution):
        from_cities = solution[:-1]
        to_cities = solution[1:]
        return np.sum(self.graph[from_cities, to_cities])

    def update_best_solution(self, solutions):
        for solution in solutions:
            cost = self.calculate_cost(solution)
            if cost < self.best_cost:
                self.best_cost = cost
                self.best_solution = solution