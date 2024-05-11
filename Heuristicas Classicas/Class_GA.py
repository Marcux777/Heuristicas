import random
import matplotlib.pyplot as plt

class GA:
    melhores_aptidoes = []
    
    def __init__(self, gene, preco):
        self.gene = gene
        self.preco = preco
        self.fit = self.calcular_fitness()

    def calcular_fitness(self):
        total_dist = self.preco[self.gene[-1] - 1][self.gene[0] - 1]
        total_dist += sum(self.preco[self.gene[i] - 1][self.gene[i + 1] - 1] for i in range(len(self.gene) - 1))
        return total_dist

    def cruzamento(self, outro):
        filho = self.gene[:]
        ponto_corte1, ponto_corte2 = sorted(random.sample(range(1, len(self.gene)), 2))
        meio_pai2 = outro.gene[ponto_corte1:ponto_corte2]
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
        return GA(filho, self.preco)

    def mutacao(self, taxa=0.01):
        if random.random() < taxa:
            i, j = sorted(random.sample(range(len(self.gene)), 2))
            self.gene[i], self.gene[j] = self.gene[j], self.gene[i]
            self.fit = self.calcular_fitness()
            
    @classmethod
    def gerar_gene_aleatorio(self, num_cidades):
        gene = list(range(1, num_cidades + 1))
        random.shuffle(gene)
        return gene
    
    @classmethod
    def calcular_fitness_media(self, populacao):
        return sum(ga.fit for ga in populacao) / len(populacao)
    
    @classmethod
    def selecionar_pais(self, populacao, taxa_selecao=0.5):
        pais = []
        while len(pais) < 2:
            for ga in populacao:
                if random.random() < taxa_selecao:
                    pais.append(ga)
        return pais

    @classmethod
    def evoluir(self, populacao, num_geracoes=100, taxa_selecao=0.5, taxa_mutacao=0.01):
        for geracao in range(num_geracoes):
            pais = self.selecionar_pais(populacao, taxa_selecao)
            filhos = []
            for i in range(len(populacao) // 2):
                pai1, pai2 = random.sample(pais, 2)
                filho = pai1.cruzamento(pai2)
                filho.mutacao(taxa_mutacao)
                filhos.append(filho)
            populacao = pais + filhos
            print("Geracao: ", geracao, " Melhor caminho:", populacao[0].gene, "\n Custo: ", round(populacao[0].fit), "\n")
            self.melhores_aptidoes.append(populacao[0].fit)
        return populacao, geracao
    
    def plotar_grafico(self):
        # Plotar o gráfico de convergência
        plt.plot(range(len(self.melhores_aptidoes)), self.melhores_aptidoes)
        plt.xlabel("Geração")
        plt.ylabel("Melhor valor de aptidão (custo do caminho)")
        plt.title("Convergência do GA para o TSP")
        plt.show()
