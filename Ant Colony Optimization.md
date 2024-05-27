# Ant Colony Optimization - Otimização Colonia de Formigas

## Intrudução

### BioInspiração

A Otimização por Colônia de Formigas (ACO) é uma técnica de otimização computacional bioinspirada no comportamento de formigas reais. Os algoritmos ACO foram inspirados em um experimento realizado por Goss et al., no qual uma colônia de formigas argentinas (Iridomyrmex humilis) tinha acesso a uma fonte de alimento em uma arena conectada ao ninho por uma ponte com dois ramos de comprimentos diferentes. As formigas, ao se deslocarem entre o ninho e a fonte de alimento, precisavam escolher um dos ramos.

Observou-se que, após uma fase inicial de exploração, a maioria das formigas passava a utilizar o ramo mais curto. Além disso, a probabilidade de a colônia escolher o ramo mais curto aumentava com a diferença de comprimento entre os dois ramos. Esse comportamento de seleção do caminho mais curto pode ser explicado em termos de autocatálise (feedback positivo) e da diferença de comprimento do caminho.
As formigas argentinas, ao se deslocarem do ninho para a fonte de alimento e vice-versa, depositam uma substância química chamada feromônio no chão. Ao chegarem a um ponto de decisão, como a interseção entre os ramos esquerdo e direito, elas fazem uma escolha probabilística, influenciada pela quantidade de feromônio que sentem em cada ramo. Este comportamento tem um efeito autocatalítico, pois o próprio ato de escolher um caminho aumenta a probabilidade de ele ser escolhido novamente por formigas futuras. No início do experimento, não há feromônio em nenhum dos ramos, portanto, as formigas que saem do ninho em direção à fonte de alimento escolherão qualquer um dos dois ramos com igual probabilidade. Devido à diferença de comprimento dos ramos, as formigas que escolherem o ramo mais curto serão as primeiras a chegar à fonte de alimento. Ao retornarem para o ninho e chegarem ao ponto de decisão, elas verão um rastro de feromônio no caminho mais curto, o rastro que elas mesmas liberaram durante a viagem de ida, e o escolherão com maior probabilidade do que o caminho mais longo.

### Definição Formal

O primeiro passo para a aplicação de ACO (Otimização por Colônia de Formigas) a um problema de otimização combinatória (COP) consiste em definir um modelo do COP como um trio (S, Ω, f), onde:

* S é o espaço de busca definido sobre um conjunto finito de variáveis de decisão discretas;
* Ω é um conjunto de restrições entre as variáveis; e
* <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>f</mi>
  <mo>:</mo>
  <mi>S</mi>
  <mo stretchy="false">&#x2192;<!-- → --></mo>
  <msubsup>
    <mi>R</mi>
    <mn>0</mn>
    <mo>+</mo>
  </msubsup>
</math> é uma função objetivo a ser minimizada (como maximizar em f é o mesmo que minimizar em -f, todo COP pode ser descrito como um problema de minimização).

O espaço de busca S é definido da seguinte forma. É dado um conjunto de variáveis discretas <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>i</mi>
  <mo>=</mo>
  <mn>1</mn>
  <mo>,</mo>
  <mo>&#x2026;<!-- … --></mo>
  <mo>,</mo>
  <mi>n</mi>
  <mtext>&#xA0;</mtext>
  <mo>,</mo>
</math> com valores <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msubsup>
    <mi>v</mi>
    <mi>i</mi>
    <mi>j</mi>
  </msubsup>
  <mo>&#x2208;<!-- ∈ --></mo>
  <msub>
    <mi>D</mi>
    <mi>i</mi>
  </msub>
  <mo>=</mo>
  <mo fence="false" stretchy="false">{</mo>
  <msubsup>
    <mi>v</mi>
    <mi>i</mi>
    <mn>1</mn>
  </msubsup>
  <mo>,</mo>
  <mo>&#x2026;<!-- … --></mo>
  <mo>,</mo>
  <msubsup>
    <mi>v</mi>
    <mi>i</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mrow class="MJX-TeXAtom-ORD">
        <mo stretchy="false">|</mo>
      </mrow>
      <msub>
        <mi>D</mi>
        <mi>i</mi>
      </msub>
      <mrow class="MJX-TeXAtom-ORD">
        <mo stretchy="false">|</mo>
      </mrow>
    </mrow>
  </msubsup>
  <mo fence="false" stretchy="false">}</mo>
  <mtext>&#xA0;</mtext>
  <mo>,</mo>
</math>. Os elementos de S são atribuições completas, ou seja, atribuições em que cada variável Xi tem um valor vⱼⁱ atribuído de seu domínio Dᵢ. O conjunto de soluções viáveis SΩ é dado pelos elementos de S que satisfazem todas as restrições no conjunto Ω.

Uma solução <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msup>
    <mi>s</mi>
    <mo>&#x2217;<!-- ∗ --></mo>
  </msup>
  <mo>&#x2208;<!-- ∈ --></mo>
  <msub>
    <mi>S</mi>
    <mi mathvariant="normal">&#x03A9;<!-- Ω --></mi>
  </msub>
</math> é chamada de ótimo global se e somente se:

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mi>f</mi>
  <mo stretchy="false">(</mo>
  <msup>
    <mi>s</mi>
    <mo>&#x2217;<!-- ∗ --></mo>
  </msup>
  <mo stretchy="false">)</mo>
  <mo>&#x2264;<!-- ≤ --></mo>
  <mi>f</mi>
  <mo stretchy="false">(</mo>
  <mi>s</mi>
  <mo stretchy="false">)</mo>
  <mtext>&#xA0;</mtext>
  <mi mathvariant="normal">&#x2200;<!-- ∀ --></mi>
  <mi>s</mi>
  <mo>&#x2208;<!-- ∈ --></mo>
  <msub>
    <mi>S</mi>
    <mi mathvariant="normal">&#x03A9;<!-- Ω --></mi>
  </msub>
  <mtext>&#xA0;</mtext>
  <mo>.</mo>
</math>

O conjunto de todas as soluções globalmente ótimas é denotado por <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msubsup>
    <mi>S</mi>
    <mi mathvariant="normal">&#x03A9;<!-- Ω --></mi>
    <mo>&#x2217;<!-- ∗ --></mo>
  </msubsup>
  <mo>&#x2286;<!-- ⊆ --></mo>
  <msub>
    <mi>S</mi>
    <mi mathvariant="normal">&#x03A9;<!-- Ω --></mi>
  </msub>
  <mtext>&#xA0;</mtext>
  <mo>.</mo>
</math>. Resolver um COP requer encontrar pelo menos um <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msup>
    <mi>s</mi>
    <mo>&#x2217;<!-- ∗ --></mo>
  </msup>
  <mo>&#x2208;<!-- ∈ --></mo>
  <msubsup>
    <mi>S</mi>
    <mi mathvariant="normal">&#x03A9;<!-- Ω --></mi>
    <mo>&#x2217;<!-- ∗ --></mo>
  </msubsup>
  <mtext>&#xA0;</mtext>
  <mo>.</mo>
</math>.


### Otimização

## Implementação

## Referências

- Dorigo, Marco & Di Caro, Gianni. (1999). The Ant Colony Optimization Meta-Heuristic. New Ideas in Optimization. (https://www.researchgate.net/publication/2831286_The_Ant_Colony_Optimization_Meta-Heuristic)

- http://www.scholarpedia.org/article/Ant_colony_optimization