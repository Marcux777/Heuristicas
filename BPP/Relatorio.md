# Relatorio

# GGA - Algoritmo Genético de Agrupamento

## Heurísticas Utilizadas

Neste trabalho, foram utilizadas diversas heurísticas para otimizar a busca por soluções. A heurística First Fit (FF) foi empregada para gerar uma solução inicial de forma rápida, distribuindo itens de maneira sequencial. O algoritmo `Tabu Search` foi então aplicado para refinar essas soluções, evitando a estagnação em ótimos locais por meio da manutenção de uma lista de soluções proibidas (tabus). Essas técnicas, em conjunto com operadores genéticos, ajudaram a explorar e explorar de forma eficiente o espaço de busca.

## Descrição do Algoritmo

O Algoritmo Genético de Agrupamento (GGA), concebido por E. Falkenauer em 1992, é uma abordagem evolutiva que visa otimizar problemas de agrupamento de dados. Diferentemente dos algoritmos genéticos tradicionais, o GGA utiliza operadores específicos para lidar com a natureza dos agrupamentos, tornando-o particularmente eficaz em problemas de alocação e particionamento de conjuntos de dados.

## Implementação

A implementação inicial do GGA utilizou operadores básicos e clássicos do algoritmo, como a seleção por torneio, cruzamento de ponto único e mutação por troca (swap mutation). 

Para gerar uma solução inicial, aplicamos a heurística First Fit (FF), que proporcionou soluções promissoras. Essa abordagem simples nos permitiu estabelecer uma base sólida para experimentação subsequente.

Para fins de comparação, utilizamos a biblioteca `Ortools` da Google nas mesmas instâncias de teste. 

Para a primeira entrada, obtivemos 44 contêineres utilizados, em comparação com os 41 contêineres obtidos pelo algoritmo do `Ortools`. 

Isso demonstrou a eficácia inicial do GGA, embora tenha revelado margem para melhorias.

![Imagem do WhatsApp de 2024-09-27 à(s) 13.07.42_bc473f22.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/896373d6-990b-4cc9-a3a2-bbb05b4e2ced/b1bedbf8-8219-4c9c-9e17-62fefc229103/Imagem_do_WhatsApp_de_2024-09-27_(s)_13.07.42_bc473f22.jpg)

A fim de aprimorar os resultados, incorporamos o algoritmo `Tabu Search`, que foi empregado para refinar as soluções parciais geradas pelo GGA. 

Cada indivíduo gerado passava por um processo de melhoria utilizando `Tabu Search`, permitindo uma busca local mais intensiva e direcionada em regiões promissoras do espaço de soluções.

Em seguida, exploramos diferentes combinações de operadores para melhorar a performance do algoritmo. 

Introduzimos métodos de seleção como o Roulette Wheel Selection e o Stoic Tournament Selection, assim como o operador de cruzamento Multi-Point Crossover. 

Também realizamos paralelização na CPU para acelerar o processo de busca. 

Essas modificações resultaram em soluções de maior qualidade, embora com um custo computacional ligeiramente superior.

![Imagem do WhatsApp de 2024-10-05 à(s) 18.56.26_3765986f.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/896373d6-990b-4cc9-a3a2-bbb05b4e2ced/b52d4343-1d64-4eff-9124-fdba203f4413/Imagem_do_WhatsApp_de_2024-10-05_(s)_18.56.26_3765986f.jpg)

Posteriormente, implementamos a mutação de inversão (Inversion Mutation) e utilizamos técnicas de otimização de hiperparâmetros, buscando identificar as configurações mais adequadas para os operadores do algoritmo. 

Isso nos permitiu obter resultados quase ótimos e, em alguns casos, atingir o valor ótimo para instâncias específicas.

![Imagem do WhatsApp de 2024-10-06 à(s) 17.47.07_e581b7c3.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/896373d6-990b-4cc9-a3a2-bbb05b4e2ced/2bdfa39b-7896-4ccd-a9e2-919c02267512/Imagem_do_WhatsApp_de_2024-10-06_(s)_17.47.07_e581b7c3.jpg)

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