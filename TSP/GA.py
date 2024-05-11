import random
import math
import matplotlib.pyplot as plt
import multiprocessing as mp

'''
GA: Classe para representar um indivíduo do GA.
'''

class GA:
    melhores_aptidoes = []
    def __init__(self, gene, preco, tabu_list=[]):
        self.gene = gene
        self.preco = preco
        self.fit = self.calcular_fitness()
        self.tabu_list = tabu_list
        
    '''
    criar_caminho(n): Cria um caminho aleatório de comprimento n.
    '''
    def criar_caminho(n):
        caminho = list(range(1, n + 1))
        random.shuffle(caminho)
        return caminho

    '''
    calcular_fitness(): Calcula o valor de aptidão do indivíduo.
    '''
    def calcular_fitness(self):
        total_dist = self.preco[self.gene[-1] - 1][self.gene[0] - 1]
        total_dist += sum(self.preco[self.gene[i] - 1][self.gene[i + 1] - 1] for i in range(len(self.gene) - 1))
        
        return total_dist

    '''
    cruzamento(outro): Cruza o indivíduo atual com outro indivíduo para criar um novo indivíduo.
    '''
    def cruzamento(self, outro):
        filho = self.gene[:]
        ponto_corte1, ponto_corte2 = sorted(random.sample(range(1, len(self.gene)), 2))
        meio_pai2 = set(outro.gene[ponto_corte1:ponto_corte2])
        pos_filho = ponto_corte2
        for gene in outro.gene:
            if gene not in meio_pai2:
                while pos_filho < len(filho) and filho[pos_filho] in meio_pai2:
                    pos_filho += 1
                    if pos_filho == len(filho):
                        pos_filho = 0
                if pos_filho < len(filho):
                    filho[pos_filho] = gene
                    pos_filho += 1
                    if pos_filho == len(filho):
                        pos_filho = 0
        return GA(filho, self.preco, self.tabu_list)
    
    def cruzamento_multiponto(self, outro, pontos=2):
        indices = sorted(random.sample(range(len(self.gene)), pontos))
        filho = self.gene[:]
        for i in range(len(indices) - 1):
            if i % 2 == 1:
                filho[indices[i]:indices[i+1]] = outro.gene[indices[i]:indices[i+1]]
        return GA(filho, self.preco, self.tabu_list)

    '''
    two_opt(): Aplica o heurístico 2-opt para melhorar o indivíduo.
    '''
    def two_opt(self):
        improved = True
        while improved:
            improved = False
            for i in range(len(self.gene) - 2):
                for j in range(i + 2, len(self.gene)-1):  # Ajuste aqui
                    if self.two_opt_ganho(i, j) < 0:
                        self.gene[i+1:j+1] = self.gene[i+1:j+1][::-1]
                        self.fit = self.calcular_fitness()
                        improved = True    

    '''
    two_opt_ganho(i, j): Calcula o ganho de aplicar o 2-opt entre as cidades i e j.
    '''
    def two_opt_ganho(self, i, j):
        a, b = self.gene[i], self.gene[i+1]

        c, d = self.gene[j], self.gene[(j+1) % len(self.gene)]

        current = self.preco[a-1][b-1] + self.preco[c-1][d-1]

        new = self.preco[a-1][c-1] + self.preco[b-1][d-1]

        return new - current

    '''
    mutacao(taxa=0.01): Aplica mutação ao indivíduo com uma taxa especificada.
    '''
    def mutacao(self, taxa=0.01):
        if random.random() < taxa:
            for _ in range(int(len(self.gene)*0.005)):  
                i, j = sorted(random.sample(range(len(self.gene)), 2))
                if abs(i - j) > 1 and (i, j) not in self.tabu_list:
                    self.gene[i], self.gene[j] = self.gene[j], self.gene[i]
                    old_fit = self.fit
                    self.fit = self.calcular_fitness()
                    self.tabu_list.append((i, j))
                    if len(self.tabu_list) > 1000:
                        self.tabu_list.pop(0)
                        
        self.two_opt()

        
    def mutacao_inversao(self, taxa=0.01):
        if random.random() < taxa:
            i, j = sorted(random.sample(range(len(self.gene)), 2))
            self.gene[i:j+1] = self.gene[i:j+1][::-1]
            self.fit = self.calcular_fitness()
        self.two_opt()
        
    '''
    ler_arquivo(caminho_arquivo): Lê os dados do TSP de um arquivo.
    '''
    def ler_arquivo(caminho_arquivo):
        with open(caminho_arquivo, 'r') as arquivo:
            n = int(arquivo.readline().strip())
            x, y = [float('inf')]*n, [float('inf')]*n
            for linha in arquivo:
                l, c1, c2 = map(float, linha.split())
                l = int(l) - 1
                x[l], y[l] = c1, c2
        return n, x, y
    
    @staticmethod
    def plot_convergencia():
        plt.figure(figsize=(10,5))
        lista = GA.melhores_aptidoes
        plt.plot(range(len(lista)), lista)
        plt.title('Convergência do Algoritmo Genético')
        plt.xlabel('Geração')
        plt.ylabel('Melhor Aptidão')
        plt.grid(True)
        plt.show()
        
    @classmethod
    def calcular_fitness_paralelo(individuo):
        total_dist = sum(individuo.preco[individuo.gene[i] - 1][individuo.gene[i + 1] - 1] for i in range(len(individuo.gene) - 1))
        return total_dist
    
    '''
    evoluir(populacao, geracoes=100): Evolui a população de indivíduos por um número especificado de gerações.
    '''
    @classmethod
    def evoluir(cls, populacao, geracoes=100):
        for geracao in range(geracoes):
            populacao.sort(key=lambda x: x.fit)
    
            print("Geracao: ", geracao, " Melhor caminho:", populacao[0].gene, "\n Custo: ", round(populacao[0].fit), "\n")
    
            novos = []
    
            melhores = populacao[:int(0.1 * len(populacao))]
   
            while len(novos) < len(populacao) - len(melhores):
                pai1, pai2 = random.sample(melhores, 2)
                filho = pai1.cruzamento(pai2)
                if random.random()>=0.43:
                    filho.mutacao()
                novos.append(filho)
                
            populacao = melhores + novos
            cls.melhores_aptidoes.append(populacao[0].fit)
        return populacao, geracao
        
    @classmethod
    def evoluir_paralelo(cls, populacao, geracoes=100):
        for geracao in range(geracoes):
            populacao.sort(key=lambda x: x.fit)

            print("Geracao: ", geracao, " Melhor caminho:", populacao[0].gene, "\n Custo: ", round(populacao[0].fit), "\n")

            novos = []

            melhores = populacao[:int(0.1 * len(populacao))]

            while len(novos) < len(populacao) - len(melhores):
                pai1, pai2 = random.sample(melhores, 2)
                filho = pai1.cruzamento(pai2)
                filho.mutacao()
                novos.append(filho)

            with mp.Pool() as pool:
                fitnesses = pool.map(cls.calcular_fitness_paralelo, novos)

            for novo, fitness in zip(novos, fitnesses):
                novo.fit = fitness

            populacao = melhores + novos
            cls.melhores_aptidoes.append(populacao[0].fit)
        return populacao, geracao
        
    