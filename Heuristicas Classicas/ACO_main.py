import math
from Ant_Colony_Optimization import ACO
import time
import math


def calculate_Weights(n, x, y):
    preco = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                preco[i][j] = math.sqrt((x[j] - x[i])**2 + (y[j] - y[i])**2)
    return preco

def read_archive(caminho_arquivo):
    x, y = [], []
    with open(caminho_arquivo, 'r') as arquivo:
        n = int(next(arquivo).strip())
        x = [float('inf')] * n
        y = [float('inf')] * n
        for linha in arquivo:
            l, c1, c2 = map(float, linha.split())
            l = int(l) - 1
            x[l], y[l] = c1, c2
    return n, x, y

pasta = "/home/marcux777/Heuristicas/Entradas/"


lista_arquivos = [
    'Djibouti.txt', 'Qatar.txt', 'Argentina.txt', 'Burma.txt', 'China.txt',
    'Egypt.txt', 'Finland.txt', 'Greece.txt', 'Honduras.txt', 'Luxembourg.txt',
    'Zimbabwe.txt', 'Uruguay.txt', 'Yemen.txt', 'Western Sahara.txt', 'Vietnam.txt',
    'Tanzania.txt', 'Sweden.txt', 'Rwanda.txt', 'Ireland.txt', 'Japan.txt',
    'Kazakhstan.txt', 'Morocco.txt', 'Nicaragua.txt', 'Oman.txt', 'Panama.txt'
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
10 - Zimbabwe.txt
11 - Uruguay.txt
12 - Yemen.txt
13 - Western Sahara.txt
14 - Vietnam.txt
15 - Tanzania.txt
16 - Sweden.txt
17 - Rwanda.txt
18 - Ireland.txt
19 - Japan.txt
20 - Kazakhstan.txt
21 - Morocco.txt
22 - Nicaragua.txt
23 - Oman.txt
24 - Panama.txt
'''

n, x, y = read_archive(pasta + lista_arquivos[1])
graph = calculate_Weights(n, x, y)

#print(ACO.find_hyperparameters(graph, 0, 100, 10)) -> returned num_ants = 50, alpha=0.8, beta=0.8, rho=0.8

aco = ACO(graph, num_ants=50, alpha=0.8, beta=0.8, rho=0.9)
start_time = time.time()
best_solution, best_cost = aco.solve(0, 100)
end_time = time.time()
print(best_solution)
print(best_cost)
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
