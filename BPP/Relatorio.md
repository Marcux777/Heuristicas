# Relatorio

## O problema do empacotamento em caixas (BPP)

O problema do empacotamento em caixas (BPP) é um problema clássico de otimização combinatória, classificado como NP-difícil, com muitas aplicações práticas em áreas como:

- Transporte e Logística
- Corte de estoque e Design de embalagens
- Alocação de recursos
- Escalonamento de máquinas

### O problema de empacotamento em caixas unidimensional (1D-BPP)

O problema de empacotamento em caixas unidimensional (1D-BPP) envolve empacotar um determinado conjunto de itens com pesos diferentes em um número mínimo de caixas, cada uma com uma capacidade fixa. O problema pode ser visto de duas maneiras:

- **Minimizar o número de caixas:** Dado um conjunto de itens e uma capacidade de caixa, encontre o menor número de caixas necessárias para empacotar todos os itens sem exceder a capacidade de qualquer caixa.
- **Minimizar a capacidade dado um número fixo de caixas (Problema Dual de Empacotamento em Caixas):** Dado um conjunto de itens e um número fixo de caixas, encontre a capacidade mínima que cada caixa deve ter para acomodar todos os itens. Essa variação também é conhecida como Problema de Escalonamento de Multiprocessadores.

### Abordagens de Solução

- **Algoritmos exatos:** Algoritmos exatos, como aqueles baseados em programação dinâmica, relaxamento LP e branch-and-bound, podem encontrar a solução ideal, mas podem ser computacionalmente caros para problemas maiores. O procedimento branch-and-bound MTP é considerado uma referência padrão para comparação na pesquisa BPP.
- **Algoritmos heurísticos e metaheurísticos:** Algoritmos heurísticos e metaheurísticos são frequentemente empregados para instâncias maiores do BPP para encontrar boas soluções de forma eficiente. Algumas das heurísticas comumente usadas incluem First-Fit Decreasing (FFD) e Best-Fit Decreasing (BFD). Esses algoritmos fornecem soluções aproximadas, mas podem nem sempre garantir a otimização.

### Técnicas de Melhoria

Pesquisadores exploraram diversas técnicas para aprimorar o desempenho das soluções BPP, incluindo:

- **Critério de Dominância:** Esta técnica sofisticada identifica e fixa caixas que dominam outras com base em seus itens embalados, reduzindo significativamente o tamanho do problema e otimizando o processo de resolução.
- **Procedimentos de Redução:** Estes procedimentos avançados simplificam a instância do problema ao identificar e eliminar itens ou caixas redundantes, seguindo regras específicas e complexas, o que resulta em uma representação mais enxuta e eficiente do problema original.
- **Abordagens Híbridas:** A combinação sinérgica de diferentes heurísticas e metaheurísticas — como algoritmos genéticos, busca tabu e simulated annealing — tem demonstrado resultados excepcionalmente promissores, aproveitando as forças de cada método para superar suas limitações individuais.
- **Processamento Paralelo:** A paralelização de algoritmos evolutivos, como os Algoritmos Genéticos de Agrupamento (GGA), utilizando técnicas avançadas como o Modelo de Ilha, pode melhorar substancialmente a exploração do espaço de busca e a qualidade da solução, permitindo uma busca mais abrangente e eficiente em menos tempo.
- **Aprendizado de Máquina:** A incorporação de técnicas de aprendizado de máquina, como redes neurais e aprendizado por reforço, está emergindo como uma abordagem promissora para melhorar a eficácia dos algoritmos de empacotamento, permitindo que eles aprendam e se adaptem a padrões específicos do problema.

### Conjuntos de Dados de Benchmark e Avaliação de Desempenho

Pesquisadores usaram vários conjuntos de dados de benchmark padrão para avaliar e comparar o desempenho de diferentes algoritmos BPP. Alguns desses conjuntos de dados incluem aqueles introduzidos por Falkenauer, que são categorizados em:

- **Uniforme (u):** Instâncias com pesos de itens distribuídos uniformemente e uma capacidade de caixa fixa.
- **Tripletos (t):** Instâncias projetadas de forma que a solução ideal envolva empacotar três itens por caixa.
- **Difícil:** Instâncias que geralmente são mais desafiadoras para resolver de forma ideal.

A avaliação do desempenho do algoritmo geralmente envolve considerar:

- **Qualidade da Solução:** Medida por métricas como o número de caixas usadas ou a quantidade de espaço desperdiçado.
- **Tempo Computacional:** O tempo necessário para encontrar uma solução.
- **Escalabilidade:** Quão bem o algoritmo se comporta à medida que o tamanho do problema aumenta.

## Complexidade Computacional do Problema de Empacotamento em Caixas

O problema do empacotamento em caixas (BPP) é classificado como **NP-difícil**, o que significa que não há algoritmo conhecido que possa resolvê-lo em tempo polinomial para todas as instâncias do problema.

**Aqui o porquê:**

- **Verificação vs. Encontrar uma Solução:** Embora seja relativamente fácil verificar se uma determinada solução para o problema de empacotamento em caixas é viável (ou seja, se todos os itens cabem nas caixas sem exceder sua capacidade), encontrar a solução ideal, que usa o menor número possível de caixas, torna-se cada vez mais difícil à medida que o número de itens e a capacidade das caixas aumentam.
- **Crescimento Exponencial de Possibilidades:** O número de maneiras possíveis de empacotar itens em caixas cresce exponencialmente com o número de itens. À medida que o tamanho do problema aumenta, mesmo os computadores mais poderosos exigiriam uma quantidade impraticável de tempo para explorar todas as combinações possíveis e garantir a descoberta da solução ideal.
- **NP-Completude:** A versão de decisão do problema de empacotamento em caixas (determinar se um conjunto de itens pode caber em um determinado número de caixas) é conhecida por ser **NP-completa**. Uma vez que a versão de otimização do problema (encontrar o número mínimo de caixas) é pelo menos tão difícil quanto a versão de decisão, ela é classificada como NP-difícil.
- **Redução de Outros Problemas NP-Completos:** A dureza NP do BPP pode ser comprovada por meio de redução, o que significa que outros problemas NP-completos conhecidos, como o problema da partição, podem ser transformados em instâncias do problema de empacotamento em caixas. Se houvesse um algoritmo de tempo polinomial para resolver o BPP, ele também poderia ser usado para resolver esses outros problemas NP-completos em tempo polinomial, o que se acredita ser impossível.

## Formulação Matemática do Problema de Empacotamento em Caixas Unidimensional

### Conjuntos:

- $N = {1, ..., n}$: Conjunto de itens a serem embalados.
- $M = {1, ..., m}$: Conjunto de caixas disponíveis.

### Parâmetros:

- $w_i$: Peso ou tamanho do item $i$, onde $i ∈ N$.
- $C$: Capacidade de cada caixa.

### Variáveis de Decisão:

- $x_{ij} = {1 \text{se o item } j \text{é atribuído à caixa} i, 0 \text{ caso contrário}}, \text{onde }i ∈ M \text{e} j ∈ N.$
- $y_i = {1 \text{se a caixa }i \text{ é usada, } 0 \text{ caso contrário}}, \text{ onde }i ∈ M.$

### Função Objetivo:

Minimizar o número total de caixas usadas:

$$
\sum_{i \in M} y_i
$$

Sujeito às seguintes restrições:

- Restrição de Capacidade: O peso total dos itens atribuídos a uma caixa não pode exceder sua capacidade:

$$
\sum_{j \in N} w_j x_{ij} \leq C y_i, \text{ para todo } i \in M
$$

- **Restrição de Atribuição:** Cada item deve ser atribuído a exatamente uma caixa:

$$
\sum_{i \in M} x_{ij} = 1, \text{ para todo } j \in N
$$

- **Restrições Binárias:** As variáveis de decisão são binárias:

$$
x_{ij} \in \{0, 1\}, \text{ para todo } i \in M, j \in N
$$

$$
y_i \in \{0, 1\}, \text{ para todo } i \in M
$$

**Explicação:**

Esta formulação visa encontrar o número mínimo de caixas ($m$) necessárias para embalar todos os itens, sujeito às restrições. A função objetivo minimiza a soma das variáveis $y_i$, que representam se uma caixa é usada ou não. As restrições garantem que a capacidade de cada caixa seja respeitada e que cada item seja atribuído a exatamente uma caixa.

**Conceitos Chave:**

- **NP-difícil:** O empacotamento em caixas é NP-difícil, o que significa que nenhum algoritmo conhecido pode resolvê-lo em tempo polinomial para todas as instâncias. Portanto, algoritmos aproximados (heurísticas) são frequentemente usados para encontrar soluções quase ideais em um tempo razoável.
- **Variáveis de Decisão:** Essas variáveis, $x_{ij}$ e $y_i$, representam as decisões que estão sendo tomadas no problema e assumem valores binários (0 ou 1) para indicar a ação escolhida.
- **Função Objetivo:** Essa função expressa matematicamente o objetivo do problema de otimização, que é minimizar o número de caixas usadas.
- **Restrições:** Essas desigualdades ou igualdades definem as soluções viáveis para o problema, garantindo que cada solução satisfaça os requisitos do problema.

Esta formulação matemática fornece uma representação concisa do 1D-BPP, permitindo a aplicação de técnicas de otimização para encontrar soluções.

# GGA - Algoritmo Genético de Agrupamento

## Descrição do Algoritmo

O Algoritmo Genético de Agrupamento (GGA), concebido por E. Falkenauer em 1992, é uma abordagem evolutiva que visa otimizar problemas de agrupamento de dados. Diferentemente dos algoritmos genéticos tradicionais, o GGA utiliza operadores específicos para lidar com a natureza dos agrupamentos, tornando-o particularmente eficaz em problemas de alocação e particionamento de conjuntos de dados.

## **Algoritmo Genético de Agrupamento (GGA) para Empacotamento em Caixas**

**Motivação para o GGA**

Algoritmos Genéticos tradicionais (GAs) muitas vezes enfrentam dificuldades em problemas de agrupamento como o BPP devido a limitações de representação e à natureza dos operadores genéticos padrão. O GGA aborda esses desafios através de:

- **Codificação Baseada em Grupos:** O GGA utiliza uma codificação onde os genes representam grupos de itens atribuídos à mesma caixa, refletindo diretamente a estrutura da solução do BPP.
- **Operadores Genéticos Especializados:** O GGA emprega operadores de cruzamento e mutação que manipulam grupos de itens, levando a uma exploração mais eficaz do espaço de solução.

**Principais Características do GGA**

- **Representação Cromossômica:**
    - **Seção de Elementos:** Representa os itens a serem embalados.
    - **Seção de Agrupamento:** Representa as caixas e os grupos de itens atribuídos a cada caixa, com comprimento variável.
- **Geração da População Inicial:**
    - Pode-se usar de heurísticas como a heurística First-Fit (FF) para criar uma população inicial de maior qualidade.
- **Função de Aptidão (Fitness):**
    - Avalia a qualidade de cada solução, considerando a plenitude ou eficiência da caixa.
- **Seleção, Cruzamento e Mutação:**
    - **Seleção:** Favorece cromossomos com valores de aptidão mais altos.
    - **Cruzamento:** Recombina cromossomos pais, preservando e propagando "boas" caixas.
    - **Mutação:** Introduz pequenas mudanças aleatórias para manter a diversidade.
- **Otimização Local:**
    - Pode-se Incorporar heurísticas de busca local, como critérios de dominância e First-Fit Decreasing (FFD).

**Vantagens do GGA**

- **Eficaz para Problemas de Agrupamento:** A codificação e os operadores especializados tornam o GGA adequado para o BPP e outros problemas de agrupamento.
- **Qualidade de Solução Melhorada:** A combinação de busca global e otimização local permite alcançar soluções de alta qualidade.

**Considerações**

- **Ajuste de Parâmetros:** Os parâmetros do GGA precisam ser ajustados para um desempenho ideal.
- **Custo Computacional:** A complexidade computacional pode ser alta para instâncias BPP muito grandes.

**Variações e Extensões**

- **GGAs Híbridos:** Combinação com outras metaheurísticas.
- **GGAs Paralelos:** Distribuição da carga de trabalho para reduzir o tempo de execução.
- **GGAs Adaptativos:** Ajuste dinâmico dos parâmetros durante a busca.

## Abordagens Híbridas Promissoras: Combinando GGAs e Heurísticas

### Hibridizar a GGA com outras heurísticas é promissor?

Sim, a hibridização de Algoritmos Genéticos de Agrupamento (GGAs) com outras heurísticas é uma abordagem muito promissora para resolver o Problema de Empacotamento em Caixas (BPP) e outros problemas de agrupamento. As fontes que você forneceu oferecem fortes evidências da eficácia de tais métodos híbridos.

### Vantagens do GGA como Base:

- **Representação Baseada em Grupos:** Os GGAs se destacam na representação de problemas de agrupamento porque sua estrutura cromossômica corresponde diretamente à estrutura inerente do problema. Cada gene em um cromossomo GGA normalmente representa um grupo de itens (uma caixa no caso do BPP), capturando naturalmente o relacionamento entre os itens dentro de um grupo. Isso é diferente dos GAs padrão, onde a representação pode não corresponder diretamente ao aspecto de agrupamento do problema, levando à interrupção de bons agrupamentos durante o cruzamento e a mutação.
- **Operadores Especializados para Agrupamento:** Os GGAs empregam operadores de cruzamento e mutação especificamente projetados para trabalhar com grupos de itens em vez de itens individuais. Essa característica é crucial para preservar e explorar agrupamentos promissores durante o processo evolutivo. Por exemplo, no contexto do BPP, o cruzamento pode envolver a troca de caixas inteiras entre soluções parentais, e a mutação pode envolver a remoção e reinserção de grupos de itens enquanto usa heurísticas para reembalá-los.

### Benefícios da Hibridização com Outras Heurísticas:

- **Busca Local Aprimorada:** Embora os GGAs se destaquem na busca global, eles podem ser aprimorados ainda mais pela integração de heurísticas de busca local para otimizar soluções dentro de cada caixa ou refinar o arranjo das caixas. Várias fontes destacam essa sinergia:
    - Um "procedimento de rearranjo simples" é usado para trocar itens entre caixas para melhorar as soluções.
    - Um procedimento de otimização local inspirado no critério de dominância é usado para melhorar as soluções após o cruzamento.
    - Os autores propõem combinar GAs com técnicas de busca local, destacando que "a sinergia entre os dois métodos pode... dar origem a uma família de algoritmos híbridos, simultaneamente globais e precisos".
- **Qualidade da População Inicial Melhorada:** Usar heurísticas para gerar a população inicial para o GGA pode melhorar significativamente o desempenho.
    - Os autores usam uma heurística de construção (First-Fit) como um decodificador para soluções, garantindo a viabilidade das soluções desde o início.
- **Abordagem de Desafios Específicos:** A hibridização permite a adaptação dos GGAs para lidar com desafios específicos frequentemente encontrados no BPP e em outros problemas de agrupamento:
    - A transmissão dos melhores genes é realizada por meio de um novo conjunto de operadores genéticos de agrupamento, enquanto a evolução é equilibrada com uma nova técnica de reprodução que controla a exploração do espaço de busca e previne a convergência prematura do algoritmo.
    - Os autores introduzem uma estratégia de restrição de tamanho do problema para reduzir a redundância no espaço de busca.

### Exemplos de GGAs Híbridos Bem-sucedidos:

As fontes consultadas fornecem exemplos de implementações bem-sucedidas de GGA híbrido:

- **GGA com Transmissão de Genes Controlada (GGA-CGT)** incorpora:
    - Uma heurística de empacotamento inteligente (FF-ñ).
    - Operadores de agrupamento inteligentes para promover a transmissão de bons genes.
    - Um procedimento de rearranjo para melhorar as soluções.
    - Uma técnica de reprodução controlada para equilibrar exploração e exploração.
- **Algoritmo Evolutivo Híbrido (HEA)** combina elementos de GGAs com outras metaheurísticas e supera outras técnicas evolutivas como C-BP e CGA-CGT.
- **Algoritmo Genético Baseado em Heurística com Bloqueio Dinâmico (HBGAwDB)** integra:
    - Uma heurística de construção (First-Fit) para decodificar soluções.
    - Monitoramento e controle dinâmico de grupos.
    - Uma estratégia de restrição de tamanho do problema.
- **Algoritmo Genético de Agrupamento Paralelo de Ilha (IPGGA)** demonstra a eficácia de combinar GGAs com:
    - Técnicas de processamento paralelo (Modelo de Ilha).
    - Várias estratégias de migração para troca de soluções entre ilhas.

## Hibridização com a GGA - Heurísticas Utilizadas

Neste trabalho, foram utilizadas diversas heurísticas para otimizar a busca por soluções. A heurística First Fit (FF) foi empregada para gerar uma solução inicial de forma rápida, distribuindo itens de maneira sequencial. O algoritmo `Tabu Search` foi então aplicado para refinar essas soluções, evitando a estagnação em ótimos locais por meio da manutenção de uma lista de soluções proibidas (tabus). Essas técnicas, em conjunto com operadores genéticos, ajudaram a explorar e explorar de forma eficiente o espaço de busca.

## Implementação

A implementação inicial do GGA utilizou operadores básicos e clássicos do algoritmo, como a seleção por torneio, cruzamento de ponto único e mutação por troca (swap mutation). 

Para gerar uma solução inicial, aplicamos a heurística First Fit (FF), que proporcionou soluções promissoras. Essa abordagem simples nos permitiu estabelecer uma base sólida para experimentação subsequente.

Para fins de comparação, utilizamos a biblioteca `Ortools` da Google nas mesmas instâncias de teste. 

Para a primeira entrada, obtivemos 44 contêineres utilizados, em comparação com os 41 contêineres obtidos pelo algoritmo do `Ortools`. 

Isso demonstrou a eficácia inicial do GGA, embora tenha revelado margem para melhorias.

![alt text](<Imagem do WhatsApp de 2024-09-27 à(s) 13.07.42_bc473f22.jpg>)

A fim de aprimorar os resultados, incorporamos o algoritmo `Tabu Search`, que foi empregado para refinar as soluções parciais geradas pelo GGA. 

Cada indivíduo gerado passava por um processo de melhoria utilizando `Tabu Search`, permitindo uma busca local mais intensiva e direcionada em regiões promissoras do espaço de soluções.

Em seguida, exploramos diferentes combinações de operadores para melhorar a performance do algoritmo. 

Introduzimos métodos de seleção como o Roulette Wheel Selection e o Stoic Tournament Selection, assim como o operador de cruzamento Multi-Point Crossover. 

Também realizamos paralelização na CPU para acelerar o processo de busca. 

Essas modificações resultaram em soluções de maior qualidade, embora com um custo computacional ligeiramente superior.

![alt text](<Captura de tela 2024-10-05 185549.png>)


Posteriormente, implementamos a mutação de inversão (Inversion Mutation) e utilizamos técnicas de otimização de hiperparâmetros, buscando identificar as configurações mais adequadas para os operadores do algoritmo. 

Isso nos permitiu obter resultados quase ótimos e, em alguns casos, atingir o valor ótimo para instâncias específicas.

![alt text](<Captura de tela 2024-10-06 174623.png>)

# Referencias

> Alvim, A.C., Ribeiro, C.C., Glover, F. *et al.* A Hybrid Improvement Heuristic for the One-Dimensional Bin Packing Problem. *Journal of Heuristics* **10**, 205–229 (2004). https://doi.org/10.1023/B:HEUR.0000026267.44673.ed
> 

> Layeb, Abdesslem & Chenche, Sara. (2012). A Novel GRASP Algorithm for Solving the Bin Packing Problem. International Journal of Information Engineering and Electronic Business. 4. 8-14. 10.5815/ijieeb.2012.02.02.
> 

> F. Luo, I. D. Scherson and J. Fuentes, "A Novel Genetic Algorithm for Bin Packing Problem in jMetal," 2017 IEEE International Conference on Cognitive Computing (ICCC), Honolulu, HI, USA, 2017, pp. 17-23, doi: 10.1109/IEEE.ICCC.2017.10. keywords: {Biological cells;Genetic algorithms;Algorithm design and analysis;Heuristic algorithms;Optimization;Genetics;Evolutionary computation;bin packing;jMetal;genetic algorithm;optimization},
> 

> Ozcan, Sukru Ozer et al. “A Novel Grouping Genetic Algorithm for the One-Dimensional Bin Packing Problem on GPU.” *International Symposium on Computer and Information Sciences* (2016).
> 

> Quiroz-Castellanos, Marcela et al. “A grouping genetic algorithm with controlled gene transmission for the bin packing problem.” *Comput. Oper. Res.* 55 (2015): 52-64.
> 

> Borgulya, István. “A hybrid evolutionary algorithm for the offline Bin Packing Problem.” *Central European Journal of Operations Research* 29 (2020): 425 - 445.
> 

> Falkenauer, Emanuel. “A hybrid grouping genetic algorithm for bin packing.” *Journal of Heuristics* 2 (1996): 5-30.
> 

> Iima, Hitoshi and Tetsuya Yakawa. “A new design of genetic algorithm for bin packing.” *The 2003 Congress on Evolutionary Computation, 2003. CEC '03.* 2 (2003): 1044-1049 Vol.2.
> 

> He, Kun et al. “Adaptive large neighborhood search for solving the circle bin packing problem.” *Comput. Oper. Res.* 127 (2021): 105140.
> 

> Abdul-Minaam, Diaa Salama et al. “An Adaptive Fitness-Dependent Optimizer for the One-Dimensional Bin Packing Problem.” *IEEE Access* 8 (2020): 97959-97974.
> 

> Cardoso Silva, Aluísio and Carlos Cristiano Hasenclever Borges. “An Improved Heuristic Based Genetic Algorithm for Bin Packing Problem.” *2019 8th Brazilian Conference on Intelligent Systems (BRACIS)* (2019): 60-65.
> 

> Scholl, Armin et al. “Bison: A fast hybrid procedure for exactly solving the one-dimensional bin packing problem.” *Comput. Oper. Res.* 24 (1997): 627-645.
> 

> Kucukyilmaz, Tayfun and Hakan Ezgi Kiziloz. “Cooperative parallel grouping genetic algorithm for the one-dimensional bin packing problem.” *Comput. Ind. Eng.* 125 (2018): 157-170.
> 

> Stawowy, Adam. “Evolutionary based heuristic for bin packing problem.” *Comput. Ind. Eng.* 55 (2008): 465-474.
> 

> Potarusov, Roman et al. “Hybrid genetic approach for 1-D bin packing problem.” *International Journal of Services Operations and Informatics* 6 (2011): 71.
> 

> Munien, Chanaleä et al. “Metaheuristic Approaches for One-Dimensional Bin Packing Problem: A Comparative Performance Study.” *IEEE Access* 8 (2020): 227438-227465.
> 

> Kaaouache, Mohamed Amine and Sadok Bouamama. “Solving bin Packing Problem with a Hybrid Genetic Algorithm for VM Placement in Cloud.” *International Conference on Knowledge-Based Intelligent Information & Engineering Systems* (2015).
> 

> Chan, Felix T. S. et al. “Using genetic algorithms to solve quality-related bin packing problem.” *Robotics and Computer-integrated Manufacturing* 23 (2007): 71-81.
> 

# Anexos

## Operadores Implementados para a GGA

### **1. Operadores de Seleção:**

- [x]  **Seleção por Roleta (Roulette Wheel Selection):**
- [x]  **Seleção por Torneio (Tournament Selection):**
- [ ]  **Seleção por Classificação (Rank Selection):**
- [ ]  **Seleção Estocástica Universal (Stochastic Universal Sampling):**
- [ ]  **Seleção Truncada (Truncation Selection):**
- [x]  Stoic Tournament Selection

---

### **2. Operadores de Cruzamento (Recombinação)**

- [x]  **Cruzamento de Ponto Único (Single-Point Crossover)**
- [x]  **Cruzamento de Múltiplos Pontos (Multi-Point Crossover)**
- [ ]  **Cruzamento Uniforme (Uniform Crossover)**
- [ ]  **Cruzamento Aritmético (Arithmetic Crossover)**
- [ ]  **Cruzamento PMX (Partially Matched Crossover)**
- [ ]  **Cruzamento de Ordem (Order Crossover - OX)**
- [ ]  **Cruzamento Cíclico (Cycle Crossover - CX)**

---

### **3. Operadores de Mutação:**

Introduzem variações aleatórias nos indivíduos para manter a diversidade genética.

- [ ]  **Mutação de Bit Flip (Bit Flip Mutation)**
- [x]  **Mutação de Troca (Swap Mutation)**
- [x]  **Mutação de Inversão (Inversion Mutation)**
- [ ]  **Mutação de Inserção (Insertion Mutation):**
- [ ]  **Mutação de Scramble (Scramble Mutation):**
- [ ]  **Mutação Gaussiana (Gaussian Mutation):**

---

### **4. Operadores de Reposição (Survivor Selection):**

- [ ]  **Reposição Geracional Completa (Generational Replacement):**
    - Toda a população é substituída pelos novos indivíduos.
    - Simples, mas pode levar à perda de boas soluções.
- [ ]  **Reposição Parcial (Steady-State Replacement):**
    - Apenas alguns indivíduos são substituídos a cada geração.
    - Mantém parte da população anterior, preservando boas soluções.
- [x]  **Elitismo:**
    - Garante que os melhores indivíduos da geração atual sejam mantidos na próxima geração.
    - Evita a perda de soluções de alta qualidade.

---

### **5. Operadores de Diversificação e Intensificação:**

- [ ]  **Diversificação:**
    - Introduz novas informações genéticas na população.
    - Evita a convergência prematura para ótimos locais.
    - Pode ser feito através de mutações mais agressivas ou reinicialização parcial da população.
- [ ]  **Intensificação:**
    - Foca na exploração profunda das áreas promissoras do espaço de busca.
    - Pode incorporar técnicas como busca local ou tabu search para melhorar soluções específicas.

---