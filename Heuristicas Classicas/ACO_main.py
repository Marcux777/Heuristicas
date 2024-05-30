import math
from Ant_Colony_Optimization import ACO


def calculate_Weights(n, x, y):
    preco = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                preco[i][j] = float(math.sqrt((x[j] - x[i])**2 + (y[j] - y[i])**2))
    return preco

def read_archive(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        n = int(arquivo.readline().strip())
        x, y = [float('inf')]*n, [float('inf')]*n
        for linha in arquivo:
            l, c1, c2 = map(float, linha.split())
            l = int(l) - 1
            x[l], y[l] = c1, c2
    return n, x, y

pasta = "/home/marcux777/Heuristicas/TSP/Entradas/"


lista_arquivos = [
    'Djibouti.txt', 'Qatar.txt', 'Argentina.txt', 'Burma.txt', 'China.txt',
    'Egypt.txt', 'Finland.txt', 'Greece.txt', 'Honduras.txt', 'Luxembourg.txt',
                  ]

'''
0 - Djibouti.txt
1 - Qatar.txt
2 - Argentina.txt
3 - Burma.txt
4 - China.txt
5 - Egypt.txt
6 - Finland.txt
7 - Greece.txt
8 - Honduras.txt
9 - Luxembourg.txt
'''

n, x, y = read_archive(pasta + lista_arquivos[0])
graph = calculate_Weights(n, x, y)

aco = ACO(graph, num_ants=50, alpha=1, beta=1, rho=0.7)

start_city = 0
max_iterations = 100
best_solution, best_cost = aco.solve(start_city, max_iterations)

print(best_solution)
print(best_cost)
