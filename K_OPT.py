import numpy as np
from itertools import combinations


def calculate_cost(solution, num_cities, distances):
    total_cost = 0
    for i in range(num_cities):
        j = (i + 1) % num_cities  # Próxima cidade na rota
        total_cost += distances[solution[i], solution[j]]
    return total_cost


def k_opt(graph, solution, k):
    def generate_k_opt_moves(solution, k):
        n = len(solution)
        if k > n:
            return []
        indices = list(range(n))
        for comb in combinations(indices, k):
            if len(set(comb)) == k:
                yield comb

    def reconnect_edges(solution, move, k):
        if k == 2:
            # Inverter o segmento entre as duas arestas removidas
            i, j = sorted(move)
            new_solution = solution[:i] + list(reversed(solution[i:j])) + solution[j:]
            yield new_solution
        elif k == 3:
            # 7 novas configurações para k = 3
            i, j, l = sorted(move)
            segments = [solution[:i], solution[i:j], solution[j:l], solution[l:]]
            # Configurações possíveis
            configs = [
                segments[0] + segments[1] + segments[2] + segments[3],
                segments[0] + segments[1] + list(reversed(segments[2])) + segments[3],
                segments[0] + list(reversed(segments[1])) + segments[2] + segments[3],
                segments[0]
                + list(reversed(segments[1]))
                + list(reversed(segments[2]))
                + segments[3],
                segments[0] + segments[2] + segments[1] + segments[3],
                segments[0] + segments[2] + list(reversed(segments[1])) + segments[3],
                segments[0] + list(reversed(segments[2])) + segments[1] + segments[3],
            ]
            for config in configs:
                yield config
        else:
            # Implementar lógica específica para k > 3
            pass

    best_solution = solution.copy()
    best_cost = calculate_cost(solution, len(graph), graph)
    improved = True

    while improved:
        improved = False
        for move in generate_k_opt_moves(solution, k):
            for new_solution in reconnect_edges(solution, move, k):
                new_cost = calculate_cost(new_solution, len(graph), graph)
                if new_cost < best_cost:
                    best_solution = new_solution
                    best_cost = new_cost
                    improved = True

        solution = best_solution

    return best_solution, best_cost
