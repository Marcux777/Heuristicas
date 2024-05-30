# Ant Colony Optimization - Otimização Colonia de Formigas


## Introdução

### Inspiração e Princípios Básicos

A Otimização por Colônia de Formigas (ACO) é um algoritmo metaheurístico inspirado no comportamento forrageiro de formigas reais. As formigas depositam rastros de feromônios enquanto se movem, guiando outras formigas para caminhos mais eficientes. A ACO imita esse comportamento usando uma população de "formigas artificiais" que constroem soluções para um problema de otimização. Cada formiga segue probabilisticamente um caminho baseado nos rastros de feromônios e em informações heurísticas.

### BioInspiração

A Otimização por Colônia de Formigas (ACO) é uma técnica de otimização computacional bioinspirada no comportamento de formigas reais. Os algoritmos ACO foram inspirados em um experimento realizado por Goss et al., no qual uma colônia de formigas argentinas (Iridomyrmex humilis) tinha acesso a uma fonte de alimento em uma arena conectada ao ninho por uma ponte com dois ramos de comprimentos diferentes. As formigas, ao se deslocarem entre o ninho e a fonte de alimento, precisavam escolher um dos ramos.

Observou-se que, após uma fase inicial de exploração, a maioria das formigas passava a utilizar o ramo mais curto. Além disso, a probabilidade de a colônia escolher o ramo mais curto aumentava com a diferença de comprimento entre os dois ramos. Esse comportamento de seleção do caminho mais curto pode ser explicado em termos de autocatálise (feedback positivo) e da diferença de comprimento do caminho.
As formigas argentinas, ao se deslocarem do ninho para a fonte de alimento e vice-versa, depositam uma substância química chamada feromônio no chão. Ao chegarem a um ponto de decisão, como a interseção entre os ramos esquerdo e direito, elas fazem uma escolha probabilística, influenciada pela quantidade de feromônio que sentem em cada ramo. Este comportamento tem um efeito autocatalítico, pois o próprio ato de escolher um caminho aumenta a probabilidade de ele ser escolhido novamente por formigas futuras. No início do experimento, não há feromônio em nenhum dos ramos, portanto, as formigas que saem do ninho em direção à fonte de alimento escolherão qualquer um dos dois ramos com igual probabilidade. Devido à diferença de comprimento dos ramos, as formigas que escolherem o ramo mais curto serão as primeiras a chegar à fonte de alimento. Ao retornarem para o ninho e chegarem ao ponto de decisão, elas verão um rastro de feromônio no caminho mais curto, o rastro que elas mesmas liberaram durante a viagem de ida, e o escolherão com maior probabilidade do que o caminho mais longo.

### Componentes Essenciais da ACO

- População de Formigas Artificiais: Um conjunto de formigas artificiais que constroem soluções para o problema de otimização.

- Rastros de Feromônios: Uma matriz que armazena a intensidade do feromônio em cada aresta do problema.

- Função de Avaliação: Uma função que mede a qualidade de uma solução construída por uma formiga artificial.

- Regras de Construção de Solução: Regras probabilísticas que guiam as formigas artificiais na construção de soluções, levando em consideração os rastros de feromônio e as informações heurísticas.

- Atualização de Feromônios: Um mecanismo que altera a intensidade dos rastros de feromônio com base na qualidade das soluções construídas.

### Caracteristicas da ACO

- ACO é baseado no comportamento coletivo das formigas: As formigas são capazes de encontrar boas fontes de alimento seguindo trilhas de feromônios deixadas por outras formigas. Os algoritmos ACO usam esse mesmo princípio para buscar boas soluções para problemas de otimização.
- Os algoritmos ACO são probabilísticos: Isso significa que há uma chance de uma formiga escolher um caminho que não é o melhor caminho. No entanto, com o tempo, as formigas têm mais probabilidade de escolher os melhores caminhos porque eles serão reforçados pelas trilhas de feromônios.
- Os algoritmos ACO são distribuídos: As formigas não precisam ter nenhum controle central. Eles podem simplesmente seguir as trilhas de feromônios uns aos outros.
- Os algoritmos ACO são robustos: Podem funcionar bem mesmo quando o problema é grande ou complexo.

### Aplicações da ACO

A ACO foi aplicada com sucesso a uma ampla gama de problemas de otimização, incluindo:

- Problema do Caixeiro Viajante (TSP): Encontrar o caminho mais curto para visitar um conjunto de cidades.

- Problema de Roteamento de Veículos (VRP): Planejar rotas eficientes para uma frota de veículos.

- Problemas de Agendamento: Atribuir tarefas a recursos com o objetivo de minimizar o tempo de conclusão ou maximizar a utilização dos recursos.

- Agrupamento de Dados: Dividir um conjunto de dados em grupos distintos com base em características comuns.

- Classificação de Dados: Prever a classe a que um novo dado pertence.

## Definição Formal

O primeiro passo para a aplicação do ACO a um problema de otimização combinatória (COP) consiste em definir um modelo do COP como uma trinca $(S,Ω,f)$, onde:

- $S$ é um espaço de busca definido sobre um conjunto finito de variáveis de decisão discretas;

- $Ω$ é um conjunto de restrições entre as variáveis; e

- $f:S→R+0$ é uma função objetivo a ser minimizada (como maximizar sobre $f$ é o mesmo que minimizar sobre $-f$, todo COP pode ser descrito como um problema de minimização).
  

O espaço de busca $S$ é definido da seguinte forma. Um conjunto de variáveis discretas $X_i$, $i=1,…,n$, com valores $v_{i}^{j} ∈ Di={v^1_i,…,v^{|Di|}_i}$, é dado. Elementos de S são atribuições completas, ou seja, atribuições nas quais cada variável $X_i$ tem um valor $v^j_i$ atribuído de seu domínio $D_i$. O conjunto de soluções viáveis $S_Ω$ é dado pelos elementos de $S$ que satisfazem todas as restrições no conjunto $Ω$.

Uma solução $s^{∗}∈ S_{Ω}$ é chamada de ótimo global se e somente se
$$f(s^{∗})≤f(s) ∀s∈S_{Ω}$$
O conjunto de todas as soluções globalmente ótimas é denotado por $S^{*}_Ω⊆S_Ω$. Resolver um COP requer encontrar pelo menos um $s^{∗}∈S^∗_Ω$.


## Implementação

[Ant Colony Optimization](/Heuristicas%20Classicas/Ant_Colony_Optimization.py)

## Referências

- Dorigo, Marco & Di Caro, Gianni. (1999). The Ant Colony Optimization Meta-Heuristic. New Ideas in Optimization. (https://www.researchgate.net/publication/2831286_The_Ant_Colony_Optimization_Meta-Heuristic)

- http://www.scholarpedia.org/article/Ant_colony_optimization

- M. Dorigo, L. M. Gambardella, M. Middendorf and T. Stutzle, "Guest editorial: special section on ant colony optimization," in IEEE Transactions on Evolutionary Computation, vol. 6, no. 4, pp. 317-319, Aug. 2002, doi: 10.1109/TEVC.2002.802446.(https://ieeexplore.ieee.org/document/1027743)

- Xu, Ben-Lian & Zhu, Jihong & Chen, Qinlan. (2010). Ant Colony Optimization. 10.5772/9389. (https://www.researchgate.net/publication/221907664_Ant_Colony_Optimization)

- M. Dorigo, M. Birattari and T. Stutzle, "Ant colony optimization," in IEEE Computational Intelligence Magazine, vol. 1, no. 4, pp. 28-39, Nov. 2006, doi: 10.1109/MCI.2006.329691. (https://ieeexplore.ieee.org/document/4129846)

- (https://www.sciencedirect.com/science/article/pii/S095219761200067X?via%3Dihub)
