# Heuristicas
 Codigo de Heuristicas e implementação de problemas clássicos com elas

## Dados - UWaterLoo

https://www.math.uwaterloo.ca/tsp/data/index.html

## Intrudução

### Metaheuristica

Imagine que você está em uma paisagem montanhosa e quer encontrar o pico mais alto. Você poderia escalar cada montanha individualmente, mas isso levaria muito tempo e esforço. Uma metaheurística seria como um guia experiente que te ajuda a navegar por essa paisagem, usando estratégias inteligentes para encontrar o pico mais alto de forma eficiente, mesmo que não seja garantido que você encontre o pico absolutamente mais alto em todas as tentativas.

Em termos mais técnicos, metaheurísticas são algoritmos de otimização de alto nível que fornecem um conjunto de diretrizes ou estratégias para projetar algoritmos heurísticos específicos para resolver uma ampla variedade de problemas de otimização. Elas são particularmente úteis quando:

* O problema é muito complexo para ser resolvido por métodos exatos em um tempo razoável.
* A função objetivo ou as restrições são não-lineares, estocásticas ou difíceis de definir matematicamente.
* Você precisa de uma boa solução em um tempo relativamente curto, mesmo que não seja a solução ótima global.

**Princípios Básicos das Metaheurísticas**

A maioria das metaheurísticas compartilha alguns princípios fundamentais:

* **Busca Iterativa:** Elas exploram o espaço de soluções de forma iterativa, gerando e avaliando novas soluções a cada iteração.
* **Uso de Memória:** Elas utilizam informações sobre as soluções já visitadas para guiar a busca futura.
* **Equilíbrio entre Exploração e Explotação:** Elas equilibram a exploração de novas regiões do espaço de soluções com a explotação de regiões promissoras já identificadas.
* **Aleatoriedade:** Elas incorporam elementos de aleatoriedade para escapar de ótimos locais e aumentar a diversidade da busca.

**Diferenças entre Metaheurísticas e Outros Métodos de Otimização**

* **Métodos Exatos:** Garantem encontrar a solução ótima global, mas podem ser computacionalmente inviáveis para problemas complexos.
* **Heurísticas:** Fornecem boas soluções em um tempo razoável, mas não garantem a otimalidade. Metaheurísticas são um tipo especial de heurística que fornece um framework geral para projetar heurísticas específicas.


[Ant Colony Optimization - ACO](/Ant%20Colony%20Optimization.md)
