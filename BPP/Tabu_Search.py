from copy import deepcopy
import random


class Tabu_Search:
    def __init__(self, gga, max_iterations=100, tabu_tenure=5, max_neighbors=100):
        """
        Initializes the Tabu Search parameters.

        Args:
            gga (GGA): An instance of the GGA class to access problem-specific methods.
            max_iterations (int): Maximum number of iterations for Tabu Search.
            tabu_tenure (int): Number of iterations a move remains in the tabu list.
            max_neighbors (int): Maximum number of neighbors to consider in each iteration.
        """
        self.gga = gga
        self.max_iterations = max_iterations
        self.tabu_tenure = tabu_tenure
        self.max_neighbors = max_neighbors

    def search(self, solution):
        """
        Applies Tabu Search to improve the given solution.

        Args:
            solution (list): The current solution to improve.

        Returns:
            list: An improved solution.
        """
        current_solution = solution
        best_solution = solution  # Avoid unnecessary deepcopy
        best_fitness = self.gga.fitness(solution)
        tabu_list = []
        iteration = 0

        while iteration < self.max_iterations:
            # Generate neighborhood with limited size
            neighborhood = self.generate_neighborhood(current_solution)

            if not neighborhood:
                break

            # Evaluate neighborhood fitness and sort
            neighborhood = [(neighbor, move, self.gga.fitness(neighbor))
                            for neighbor, move in neighborhood]
            # Sort by fitness (lower is better)
            neighborhood.sort(key=lambda x: x[2])

            found = False
            for neighbor, move, fitness in neighborhood:
                if move not in tabu_list or fitness < best_fitness:
                    # Update tabu list
                    tabu_list.append(move)
                    if len(tabu_list) > self.tabu_tenure:
                        tabu_list.pop(0)

                    current_solution = neighbor

                    if fitness < best_fitness:
                        best_solution = neighbor  # No need to deepcopy
                        best_fitness = fitness

                    found = True
                    break  # Move to the next iteration after finding a valid neighbor

            if not found:
                break  # No valid moves found; terminate search

            iteration += 1

        return best_solution

    def generate_neighborhood(self, solution):
        """
        Generates neighboring solutions by moving elements between containers,
        limiting the number of neighbors to max_neighbors.

        Args:
            solution (list): The current solution.

        Returns:
            list: A list of tuples (neighbor_solution, move).
        """
        neighbors = []
        n = len(solution)
        count = 0

        # Precompute possible moves and shuffle them to add randomness
        possible_moves = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    possible_moves.append((i, j))

        random.shuffle(possible_moves)

        for i, j in possible_moves:
            elements = solution[i].elements.copy()
            random.shuffle(elements)
            for element in elements:
                if solution[j].remaining_space() >= element:
                    # Create new solution with minimal copying
                    new_solution = solution.copy()  # Shallow copy of the solution list
                    # Copy only the modified containers
                    new_solution[i] = solution[i].copy()
                    new_solution[j] = solution[j].copy()
                    # Move the element
                    new_solution[i].remove_element(element)
                    new_solution[j].add_element(element)
                    # Remove empty containers
                    new_solution = self.gga._remove_empty_containers(
                        new_solution)
                    # Record the move
                    from_container_id = id(solution[i])
                    to_container_id = id(solution[j])
                    move = (element, from_container_id, to_container_id)
                    neighbors.append((new_solution, move))
                    count += 1
                    if count >= self.max_neighbors:
                        return neighbors
        return neighbors
