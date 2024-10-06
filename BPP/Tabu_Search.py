import random


class Tabu_Search:
    def __init__(self, gga, max_iterations=100, tabu_tenure=5, max_neighbors=100):
        self.gga = gga
        self.max_iterations = max_iterations
        self.tabu_tenure = tabu_tenure
        self.max_neighbors = max_neighbors
        self.tabu_list = set()

    def search(self, solution):
        current_solution = solution
        best_solution = solution
        best_fitness = self.gga.fitness(solution)
        iteration = 0

        while iteration < self.max_iterations:
            neighborhood = self.generate_neighborhood(current_solution)
            if not neighborhood:
                break

            neighborhood = sorted(neighborhood, key=lambda x: x[2])
            for neighbor, move, fitness in neighborhood:
                if move not in self.tabu_list or fitness < best_fitness:
                    self.tabu_list.add(move)
                    if len(self.tabu_list) > self.tabu_tenure:
                        self.tabu_list.pop()

                    current_solution = neighbor
                    if fitness < best_fitness:
                        best_solution = neighbor
                        best_fitness = fitness
                    break

            iteration += 1

        return best_solution

    def generate_neighborhood(self, solution):
        neighbors = []
        n = len(solution)

        possible_moves = [(i, j) for i in range(n) for j in range(n) if i != j]
        random.shuffle(possible_moves)

        for i, j in possible_moves:
            elements = solution[i].elements.copy()
            random.shuffle(elements)
            for element in elements:
                if solution[j].remaining_space() >= element:
                    new_solution = solution.copy()
                    new_solution[i] = solution[i].copy()
                    new_solution[j] = solution[j].copy()

                    new_solution[i].remove_element(element)
                    new_solution[j].add_element(element)
                    new_solution = self.gga._remove_empty_containers(
                        new_solution)

                    move = (element, id(solution[i]), id(solution[j]))
                    neighbors.append(
                        (new_solution, move, self.gga.fitness(new_solution)))

                    if len(neighbors) >= self.max_neighbors:
                        return neighbors

        return neighbors
