
# O Problema do Caixeiro Viajante



# 1° Solução Encontrada - Hibridização de Algoritmos com GA

## Algoritmo Genetico (GA - Genetic Algorithm)

O Algoritmo Genético (GA) é uma metaheurística inspirada no processo de seleção natural. É uma ferramenta poderosa para resolver problemas de otimização, incluindo o Problema do Caixeiro Viajante (PCV).

### Como funciona
O GA começa com uma população de soluções geradas aleatoriamente, chamadas cromossomos. Cada cromossomo representa uma possível solução para o PCV. Os cromossomos são então avaliados com base em sua aptidão, que é uma medida de quão bons eles são na resolução do problema.

O GA então usa um processo de seleção, cruzamento e mutação para criar uma nova geração de cromossomos. A seleção escolhe os cromossomos mais aptos da população atual para serem pais da próxima geração. O cruzamento combina o material genético de dois cromossomos pais para criar novos cromossomos filhos. A mutação introduz mudanças aleatórias nos cromossomos filhos.

O processo de seleção, cruzamento e mutação é repetido por um número de gerações. Com o tempo, o GA converge para uma população de cromossomos que são cada vez melhores na resolução do PCV.

### Vantagens
- O GA é um algoritmo de otimização poderoso e versátil que pode ser aplicado a uma ampla gama de problemas.
- O GA é relativamente fácil de implementar.
- O GA pode encontrar boas soluções para o PCV, mesmo para grandes instâncias de problemas.

### Desvantagens

- O GA pode ser lento para convergir para uma boa solução.
- O GA pode ser sensível à escolha de parâmetros, como o tamanho da população e a taxa de mutação.

## K-Opt Search (Busca K-Opt)
A busca K-Opt é um algoritmo de busca local usado para resolver o Problema do Caixeiro Viajante (PCV). Ele funciona melhorando iterativamente uma solução dada, fazendo pequenas alterações nela.

### Como funciona
A busca K-Opt começa com uma solução inicial, que pode ser gerada aleatoriamente ou usando outra heurística. Em seguida, explora iterativamente a vizinhança da solução atual, fazendo pequenas alterações nela. Essas alterações são chamadas de "movimentos K-Opt", onde K é o número de arestas que são alteradas no movimento.

Por exemplo, um movimento 2-Opt envolveria a troca de duas arestas na solução. Um movimento 3-Opt envolveria a troca de três arestas, e assim por diante. 
No caso do código implementado, é 2-opt.

A busca K-Opt avalia cada solução vizinha e mantém a melhor. Este processo é repetido até que nenhuma melhoria adicional possa ser feita.

### Vantagens
- A busca K-Opt é relativamente fácil de implementar.
- Pode encontrar boas soluções para o PCV, especialmente para pequenas instâncias de problemas.
### Desvantagens
- A busca K-Opt pode ficar presa em ótimos locais, que são soluções que não são o ótimo global, mas são melhores do que qualquer uma de suas soluções vizinhas.
- A busca K-Opt pode ser lenta para grandes instâncias de problemas.

## Tabu Search

A Busca Tabu é outro algoritmo de busca local que pode ser usado para resolver o Problema do Caixeiro Viajante (PCV). É semelhante à busca K-Opt, pois melhora iterativamente uma solução dada, fazendo pequenas alterações nela. No entanto, a Busca Tabu usa uma estrutura de memória para evitar que a busca revisite soluções que já foram exploradas. Isso ajuda a evitar ficar preso em ótimos locais¹².

### Como funciona
A Busca Tabu começa com uma solução inicial, assim como a busca K-Opt. Em seguida, explora a vizinhança da solução atual e identifica a melhor solução vizinha. No entanto, antes de aceitar essa solução, a Busca Tabu verifica sua estrutura de memória para ver se a solução já foi visitada. Se foi, a solução é rejeitada e a busca continua. Caso contrário, a solução é aceita e adicionada à estrutura de memória¹².

A estrutura de memória na Busca Tabu é tipicamente uma lista de soluções recentemente visitadas. O tamanho da lista é chamado de permanência tabu. A permanência tabu determina quanto tempo uma solução permanece na estrutura de memória. Depois que uma solução esteve na estrutura de memória pelo tempo de permanência tabu, ela é removida da lista e pode ser considerada novamente¹².

### Vantagens
- A Busca Tabu é menos provável de ficar presa em ótimos locais do que a busca K-Opt.
- A Busca Tabu pode encontrar melhores soluções do que a busca K-Opt, especialmente para grandes instâncias de problemas¹².

### Desvantagens
- A Busca Tabu é mais complexa para implementar do que a busca K-Opt.
- A Busca Tabu pode ser mais lenta do que a busca K-Opt.

Aqui está como a Busca Tabu pode funcionar para o PCV:

1. Comece com uma solução inicial.
2. Explore a vizinhança da solução atual e identifique a melhor solução vizinha.
3. Verifique a estrutura de memória para ver se a solução já foi visitada.
4. Se a solução não foi visitada, aceite-a e adicione-a à estrutura de memória.
5. Se a solução foi visitada, rejeite-a e continue explorando a vizinhança.
6. Repita os passos 2-5 até que um critério de parada seja atendido.

## Maquina:
- Processador: Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz   1.19 GHz
- RAM instalada: 8,00 GB (utilizável: 7,77 GB)
- Tipo de sistema: Sistema operacional de 64 bits, processador baseado em x64
- Sistema Operacional: Windows 11 Home Single Language
- Placa de Video: NVIDIA GeForce MX350

## Resultados:

| Instância | Pais|  Optimal Tour |Valor Tour Obtido | Tempo(s) |
|---|---|---|---|---|
| 38 | Djibouti | 6656 | 6659 | 8.35 |
| 194 | Qatar | 9352 | 9395 |  276.72 |
| 980 | Luxemburgo | 11340 | 11590 | 9864.16
