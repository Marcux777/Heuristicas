import random
from collections import deque


class Tabu_Search:
    def __init__(self, gga, max_iterations=100, tabu_tenure=5, max_neighbors=100):
        self.gga = gga
        self.max_iterations = max_iterations
        self.tabu_tenure = tabu_tenure
        self.max_neighbors = max_neighbors
        self.tabu_list = deque(maxlen=self.tabu_tenure)
        self.tabu_set = set()

    def search(self, solution):
        current_solution = solution
        best_solution = solution
        best_fitness = self.gga.fitness(solution)
        iteration = 0

        while iteration < self.max_iterations:
            neighbor_found = False
            neighbors = self.generate_neighborhood(current_solution)
            for neighbor, move, fitness in neighbors:
                if move not in self.tabu_set or fitness < best_fitness:
                    # Atualiza o tabu list
                    self.tabu_list.append(move)
                    self.tabu_set.add(move)
                    if len(self.tabu_list) > self.tabu_tenure:
                        oldest_move = self.tabu_list.popleft()
                        self.tabu_set.remove(oldest_move)

                    current_solution = neighbor
                    if fitness < best_fitness:
                        best_solution = neighbor
                        best_fitness = fitness
                    neighbor_found = True
                    break  # Move para a próxima iteração

            if not neighbor_found:
                break  # Nenhum vizinho aceitável encontrado

            iteration += 1

        return best_solution

    def generate_neighborhood(self, solution):
        neighbors = []
        n = len(solution)
        attempts = 0
        max_attempts = self.max_neighbors * 10  # Limite para evitar loops infinitos

        while len(neighbors) < self.max_neighbors and attempts < max_attempts:
            attempts += 1
            i, j = random.sample(range(n), 2)
            container_i = solution[i]
            container_j = solution[j]

            if not container_i.elements:
                continue

            element = random.choice(container_i.elements)
            if container_j.remaining_space() >= element:
                # Cria uma nova solução aplicando o movimento
                new_solution = solution.copy()
                new_solution[i] = container_i.copy()
                new_solution[j] = container_j.copy()
                new_solution[i].remove_element(element)
                new_solution[j].add_element(element)
                new_solution = self.gga._remove_empty_containers(new_solution)

                move = (element, i, j)
                fitness = self.gga.fitness(new_solution)
                neighbors.append((new_solution, move, fitness))

        return neighbors
