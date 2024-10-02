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
            i, j = sorted(move)
            return [solution[:i] + list(reversed(solution[i:j])) + solution[j:]]
        elif k == 3:
            i, j, l = sorted(move)
            a, b, c, d = solution[:i], solution[i:j], solution[j:l], solution[l:]
            return [
                a + b + c + d,
                a + b + c[::-1] + d,
                a + b[::-1] + c + d,
                a + b[::-1] + c[::-1] + d,
                a + c + b + d,
                a + c + b[::-1] + d,
                a + c[::-1] + b + d,
            ]
        else:
            # Simplificação para k > 3 usando rotações
            n = len(solution)
            move = sorted(move) + [move[0] + n]  # Fecha o ciclo
            best_solution = solution
            best_cost = calculate_cost(solution, len(graph), graph)

            for i in range(1, k):
                for j in range(i + 2, k + 1):
                    new_solution = solution[:]
                    new_solution[move[i - 1] : move[j]] = solution[
                        move[j - 1] : move[i - 1] : -1
                    ]
                    new_cost = calculate_cost(new_solution, len(graph), graph)
                    if new_cost < best_cost:
                        best_solution = new_solution
                        best_cost = new_cost
            return [best_solution]

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


"""graph = np.array(
    [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
)

# Solução inicial (pode ser qualquer permutação válida)
solution = [0, 1, 2, 3]

# Valor de k para o k-opt
k = 2

# Executa o k-opt
best_solution, best_cost = k_opt(graph, solution, k)

# Imprime os resultados
print("Melhor solução:", best_solution)
print("Melhor custo:", best_cost)
"""
