import random
from collections import deque


class Tabu_Search:
    def __init__(self, gga, max_iterations=100, tabu_tenure=5, max_neighbors=100):
        """
        Inicializa o algoritmo de Busca Tabu com os parâmetros fornecidos.

        Args:
            gga (object): O objeto do algoritmo genético a ser utilizado.
            max_iterations (int, opcional): O número máximo de iterações para a Busca Tabu. Padrão é 100.
            tabu_tenure (int, opcional): O número de iterações que um movimento permanece na lista tabu. Padrão é 5.
            max_neighbors (int, opcional): O número máximo de vizinhos a considerar em cada iteração. Padrão é 100.
        """
        self.gga = gga
        self.max_iterations = max_iterations
        self.tabu_tenure = tabu_tenure
        self.max_neighbors = max_neighbors
        self.tabu_list = deque(maxlen=self.tabu_tenure)
        self.tabu_set = set()

    def search(self, solution):
        """
        Realiza uma Busca Tabu para encontrar a melhor solução.

        Args:
            solution (list): A solução inicial para começar a busca.

        Returns:
            list: A melhor solução encontrada durante a busca.

        A função explora iterativamente a vizinhança da solução atual,
        atualizando a melhor solução encontrada e mantendo uma lista tabu para evitar ciclos.
        A busca para quando o número máximo de iterações é alcançado ou nenhum
        vizinho aceitável é encontrado.
        """
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
        """
        Gera uma vizinhança de soluções movendo elementos entre contêineres.

        Args:
            solution (list): A solução atual representada como uma lista de contêineres.

        Returns:
            list: Uma lista de tuplas, cada uma contendo uma nova solução, o movimento realizado e a aptidão da nova solução.

        A função tenta gerar um número especificado de soluções vizinhas selecionando aleatoriamente dois contêineres
        e movendo um elemento de um contêiner para outro, se houver espaço suficiente. Ela garante que o número de vizinhos
        não exceda `self.max_neighbors` e evita loops infinitos limitando o número de tentativas. Cada nova solução
        é avaliada quanto à sua aptidão, e contêineres vazios são removidos antes de adicionar a solução à lista de vizinhos.
        """
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
