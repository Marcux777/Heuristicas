from Genetic_Algorithm import GA
import random
import matplotlib.pyplot as plt

melhores_aptidoes = []

# Definindo o número de cidades e a matriz de distâncias
n = 5
preco = [[0, 10, 15, 20, 25],
         [10, 0, 35, 25, 20],
         [15, 35, 0, 30, 15],
         [20, 25, 30, 0, 10],
         [25, 20, 15, 10, 0]]

# Criando a população inicial
populacao = [GA(GA.generate_random_gene(n), preco) for _ in range(10)]

# Evoluindo a população
resultados, geracao = GA.evolve(populacao)

print("Geracao: ", geracao, " Melhor caminho:", resultados[0].gene, "\n Custo: ", round(resultados[0].fit), "\n")