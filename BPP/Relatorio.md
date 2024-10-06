## GGA

Durante a implementação da GGA

### **1. Operadores de Seleção:**

- [x] **Seleção por Roleta (Roulette Wheel Selection):**

- [ ] **Seleção por Torneio (Tournament Selection):**

- [ ] **Seleção por Classificação (Rank Selection):**

- [ ] **Seleção Estocástica Universal (Stochastic Universal Sampling):**

- [ ] **Seleção Truncada (Truncation Selection):**

---

### **2. Operadores de Cruzamento (Recombinação):**


- **Cruzamento de Ponto Único (Single-Point Crossover):**

- **Cruzamento de Múltiplos Pontos (Multi-Point Crossover):**

- **Cruzamento Uniforme (Uniform Crossover):**

- **Cruzamento Aritmético (Arithmetic Crossover):**

- **Cruzamento PMX (Partially Matched Crossover):**

- **Cruzamento de Ordem (Order Crossover - OX):**

- **Cruzamento Cíclico (Cycle Crossover - CX):**

---

### **3. Operadores de Mutação:**

Introduzem variações aleatórias nos indivíduos para manter a diversidade genética.

- **Mutação de Bit Flip (Bit Flip Mutation):**
  - Inverte o valor de um gene binário (0 para 1 ou 1 para 0).
  - Simples e comum em cromossomos binários.

- **Mutação de Troca (Swap Mutation):**
  - Troca a posição de dois genes.
  - Útil para problemas de permutação.

- **Mutação de Inversão (Inversion Mutation):**
  - Inverte a sequência de genes entre dois pontos.
  - Preserva os genes mas altera a ordem.

- **Mutação de Inserção (Insertion Mutation):**
  - Remove um gene e o insere em outra posição.
  - Altera a posição de um único gene.

- **Mutação de Scramble (Scramble Mutation):**
  - Embaralha aleatoriamente os genes em uma subsequência selecionada.
  - Mantém os mesmos genes mas muda a ordem.

- **Mutação Gaussiana (Gaussian Mutation):**
  - Adiciona um valor aleatório, seguindo uma distribuição normal, a um gene numérico.
  - Adequado para cromossomos com genes contínuos.

---

### **4. Operadores de Reposição (Survivor Selection):**

Determinano quais indivíduos permanecerão na população após a criação dos novos indivíduos.

- **Reposição Geracional Completa (Generational Replacement):**
  - Toda a população é substituída pelos novos indivíduos.
  - Simples, mas pode levar à perda de boas soluções.

- **Reposição Parcial (Steady-State Replacement):**
  - Apenas alguns indivíduos são substituídos a cada geração.
  - Mantém parte da população anterior, preservando boas soluções.

- **Elitismo:**
  - Garante que os melhores indivíduos da geração atual sejam mantidos na próxima geração.
  - Evita a perda de soluções de alta qualidade.

---

### **5. Operadores de Diversificação e Intensificação:**

- **Diversificação:**
  - Introduz novas informações genéticas na população.
  - Evita a convergência prematura para ótimos locais.
  - Pode ser feito através de mutações mais agressivas ou reinicialização parcial da população.

- **Intensificação:**
  - Foca na exploração profunda das áreas promissoras do espaço de busca.
  - Pode incorporar técnicas como busca local ou tabu search para melhorar soluções específicas.

---
