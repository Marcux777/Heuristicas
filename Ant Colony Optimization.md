# Ant Colony Optimization - Otimização Colonia de Formigas

## Intrudução

### BioInspiração

A Otimização por Colônia de Formigas (ACO) é uma técnica de otimização computacional bioinspirada no comportamento de formigas reais. Os algoritmos ACO foram inspirados em um experimento realizado por Goss et al., no qual uma colônia de formigas argentinas (Iridomyrmex humilis) tinha acesso a uma fonte de alimento em uma arena conectada ao ninho por uma ponte com dois ramos de comprimentos diferentes. As formigas, ao se deslocarem entre o ninho e a fonte de alimento, precisavam escolher um dos ramos.

Observou-se que, após uma fase inicial de exploração, a maioria das formigas passava a utilizar o ramo mais curto. Além disso, a probabilidade de a colônia escolher o ramo mais curto aumentava com a diferença de comprimento entre os dois ramos. Esse comportamento de seleção do caminho mais curto pode ser explicado em termos de autocatálise (feedback positivo) e da diferença de comprimento do caminho.
As formigas argentinas, ao se deslocarem do ninho para a fonte de alimento e vice-versa, depositam uma substância química chamada feromônio no chão. Ao chegarem a um ponto de decisão, como a interseção entre os ramos esquerdo e direito, elas fazem uma escolha probabilística, influenciada pela quantidade de feromônio que sentem em cada ramo. Este comportamento tem um efeito autocatalítico, pois o próprio ato de escolher um caminho aumenta a probabilidade de ele ser escolhido novamente por formigas futuras. No início do experimento, não há feromônio em nenhum dos ramos, portanto, as formigas que saem do ninho em direção à fonte de alimento escolherão qualquer um dos dois ramos com igual probabilidade. Devido à diferença de comprimento dos ramos, as formigas que escolherem o ramo mais curto serão as primeiras a chegar à fonte de alimento. Ao retornarem para o ninho e chegarem ao ponto de decisão, elas verão um rastro de feromônio no caminho mais curto, o rastro que elas mesmas liberaram durante a viagem de ida, e o escolherão com maior probabilidade do que o caminho mais longo.

### Definição Formal

O primeiro passo para a aplicação do ACO a um problema de otimização combinatória (COP) consiste em definir um modelo do COP como uma trinca $(S,Ω,f)$, onde:

- $S$ é um espaço de busca definido sobre um conjunto finito de variáveis de decisão discretas;

- $Ω$ é um conjunto de restrições entre as variáveis; e

- $f:S→R+0$ é uma função objetivo a ser minimizada (como maximizar sobre $f$ é o mesmo que minimizar sobre $-f$, todo COP pode ser descrito como um problema de minimização).
  

O espaço de busca $S$ é definido da seguinte forma. Um conjunto de variáveis discretas $X_i$, $i=1,…,n$, com valores $v^j_i ∈ Di={v^1_i,…,v^{|Di|}_i}$, é dado. Elementos de S são atribuições completas, ou seja, atribuições nas quais cada variável $X_i$ tem um valor $v^{j}_{i}$ atribuído de seu domínio $D_i$. O conjunto de soluções viáveis $S_Ω$ é dado pelos elementos de $S$ que satisfazem todas as restrições no conjunto $Ω$.

Uma solução $s^{∗}∈ S_{Ω}$ é chamada de ótimo global se e somente se
$$f(s^{∗})≤f(s) ∀s∈S_{Ω}$$
O conjunto de todas as soluções globalmente ótimas é denotado por $S^{*}_Ω⊆S_Ω$. Resolver um COP requer encontrar pelo menos um $s^{∗}∈S^∗_Ω$.


### Otimização

## Implementação

## Referências

- Dorigo, Marco & Di Caro, Gianni. (1999). The Ant Colony Optimization Meta-Heuristic. New Ideas in Optimization. (https://www.researchgate.net/publication/2831286_The_Ant_Colony_Optimization_Meta-Heuristic)

- http://www.scholarpedia.org/article/Ant_colony_optimization

- https://ieeexplore.ieee.org/document/1027743

- https://www.researchgate.net/publication/221907664_Ant_Colony_Optimization

- https://ieeexplore.ieee.org/document/4129846

- https://www.sciencedirect.com/science/article/pii/S095219761200067X?via%3Dihub
