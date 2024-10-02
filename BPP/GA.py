import random


class Item():
    def __init__(self, peso, indice):
        self.peso = 0
        self.indice = 0


class Conteiner():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.lista_de_itens = []

    def __init__(self, capacidade, lista):
        self.capacidade = capacidade
        self.lista_de_itens = lista

    def add_item(self, item):
        self.lista_de_itens.append(item)

    def remove_item(self, item):
        self.lista_de_itens.remove(item)


class GA():
    def __init__(
        self,
        populacao,
        X_rate,
        P_rate,
        max_itens,
        max_peso,
    ):
        self.populacao = populacao
        self.X_rate = X_rate
        self.P_rate = P_rate
        self.max_itens = max_itens
        self.max_peso = max_peso

    def create_population(self):
        self.population = []
        for i in range(self.populacao):
            self.population.append(self.create_individual())

    def create_individual(self):
        individual = []
        for i in range(self.max_itens):
            individual.append(random.randint(0, 1))
        return individual

    def fitness(self, solucao, pesos):
        """
        Calcula a função de aptidão (fitness) de uma solução.
        Objetivo: Minimizar o número de bins usados.
        """
        bins_usados = 1
        capacidade_atual = self.capacidade

        for item in solucao:
            if pesos[item] <= capacidade_atual:
                capacidade_atual -= pesos[item]
            else:
                bins_usados += 1
                capacidade_atual = self.capacidade - pesos[item]

        return bins_usados

    def selecao(self, populacao, pesos):
        """
        Seleciona os pais para o cruzamento usando o método da roleta.
        """
        aptidoes = [self.fitness(solucao, pesos) for solucao in populacao]
        soma_aptidoes = sum(aptidoes)
        probabilidades = [aptidao / soma_aptidoes for aptidao in aptidoes]

        pais = []
        for _ in range(2):  # Seleciona 2 pais
            r = random.random()
            soma_probabilidades = 0
            for i, probabilidade in enumerate(probabilidades):
                soma_probabilidades += probabilidade
                if soma_probabilidades >= r:
                    pais.append(populacao[i])
                    break
        return pais

    def cruzamento(self, pai1, pai2):
        """
        Realiza o cruzamento (crossover) entre dois pais.
        """
        ponto_corte = random.randint(1, self.n_itens - 1)
        filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
        filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
        return filho1, filho2

    def mutacao(self, solucao):
        for i in range(self.max_itens):
            if random.random() < self.P_rate:
                j = random.randint(0, self.n_itens - 1)
                solucao[i], solucao[j] = solucao[j], solucao[i]
        return solucao
