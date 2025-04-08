---
title: Basics to Bayes
weight: 1
---

## Introdução

### Espaços Amostrais e Eventos

O espaço amostral $\Omega$ é o conjunto de possíveis resultados de um experimento. Os pontos $\omega$ em $\Omega$ são chamados de resultados amostrais, realizações ou elementos. Subconjuntos de $\Omega$ são chamados de eventos. 


#### Exemplo 1.3

Se lançarmos uma moeda para sempre, então o espaço amostral é o conjunto infinito:

$$
\Omega = \left\{ \omega = (\omega_1, \omega_2, \omega_3, \dots) : \omega_i \in \{H, T\} \right\}.
$$

Seja $E$ o evento em que a primeira face "cara" ($H$) aparece no terceiro lançamento. Então:

$$
E = \left\{ (\omega_1, \omega_2, \omega_3, \dots) : \omega_1 = T, \omega_2 = T, \omega_3 = H, \, \omega_i \in \{H, T\} \text{ para } i > 3 \right\}.
$$


#### Exemplo prático 1

Suponha que lancemos uma moeda justa até obtermos exatamente duas caras. Descreva o espaço amostral $S$.


### Conjuntos disjuntos

Dizemos que $A_1, A_2, \dots $ são disjuntos ou mutuamente exclusivos se  

$$
A_i \cap A_j = \emptyset \quad \text{sempre que } i \neq j.
$$

Por exemplo, os conjuntos  

$
A_1 = [0,1), \quad A_2 = [1,2), \quad A_3 = [2,3), \dots
$ 

são disjuntos.

Uma partição de $\Omega$ é uma sequência de conjuntos disjuntos $A_1, A_2, \dots $ tal que  

$$
\bigcup_{i=1}^{\infty} A_i = \Omega.
$$


### Sequências Monótonas de Conjuntos

![Sequências Monótonas de Conjuntos](monotone-increasing.png "Sequências Monótonas de Conjuntos")

Uma sequência de conjuntos $A_1, A_2, \dots $ é **monotonamente crescente** se $A_1 \subset A_2 \subset A_3 \subset \dots$ e definimos 

$$
\lim_{n \to \infty} A_n = \bigcup_{i=1}^{\infty} A_i.
$$

Uma sequência de conjuntos $A_1, A_2, \dots $ é **monotonamente decrescente** se 
$A_1 \supset A_2 \supset A_3 \supset \dots$
e definimos 

$$
\lim_{n \to \infty} A_n = \bigcap_{i=1}^{\infty} A_i.
$$

Em ambos os casos, escrevemos $A_n \to A$.


### Sumário das terminologias básicas

| Símbolo        | Descrição                                     |
|----------------|-------------------------------------------------|
| $\Omega$      | espaço amostral (Letra Ômega nessa apresentação) |
| $\omega$     | resultado (ponto ou elemento)                 |
| $A$           | evento (subconjunto de $\Omega$)              |
| $A^c$         | complemento de $A$ (não $A$)                  |
| $A \cup B$   | união ($A$ ou $B$)                            |
| $A \cap B$ ou $AB$ | interseção ($A$ e $B$)                      |
| $A - B$       | diferença de conjuntos ($\omega$ em $A$, mas não em $B$) |
| $A \subset B$ | inclusão de conjuntos                         |
| $\emptyset$  | evento nulo (sempre falso)                    |
| $\Omega$      | evento certo (sempre verdadeiro (?))          |


## Probabilidade

### Interpretações Possíveis

O livro trás duas visões diferentes de como entender probabilidade.
- **Frequentista:** A probabilidade de um evento é, em um grande número de experimentações, a proporção de vezes que um evento é verdadeiro ao longo da repetição. ([link](https://digitalfirst.bfwpub.com/stats_applet/stats_applet_10_prob.html))
- **Bayesiana:** A crença de um observador em que um determinado evento é verdadeiro.

### Definição de Probabilidade

**Definição.** Uma função $\mathbb{P}$ que atribui um número real $\mathbb{P}(A)$ para cada evento $A$ é uma **distribuição de probabilidade** ou uma **medida de probabilidade** se satisfaz os seguintes três axiomas:

- **Axioma 1:** $\mathbb{P}(A) \geq 0$ para cada $A$
- **Axioma 2:** $\mathbb{P}(\Omega) = 1$
- **Axioma 3:** Se $A_1, A_2, \dots$ são disjuntos, então
    $$
    \mathbb{P} \left( \bigcup_{i=1}^{\infty} A_i \right) = \sum_{i=1}^{\infty} \mathbb{P}(A_i).
    $$

Isso cria algumas implicações interessantes das quais devemos estar cientes:
- $\mathbb{P}(\emptyset) = 0$
- $A \subset B \implies \mathbb{P}(A) \leq \mathbb{P}(B)$
- $0 \leq \mathbb{P}(A) \leq 1$
- $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$
- $A \cap B = \emptyset \implies \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B). \quad $

### União de Eventos
**Lema.** *Para cada evento $A$ e $B$,*

$$
\mathbb{P} \left( A \cup B \right) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(AB).
$$


*Obs: Veja a prova na página 6.

### Continuidade de Probabilidades
**Teorema (Continuidade de Probabilidades).**
If $A_n \to A$ then
$$
P(A_n) \to P(A) \quad \text{as } n \to \infty.
$$


## Eventos Independentes

**Definição**: Dois eventos \( A \) e \( B \) são independentes se
$$
P(A B) = P(A) P(B) = P(A) \cdot P(B)
$$
e escrevemos \( A\perp\!\!\!\perp B \) (Lê-se A é independente de B). Um conjunto de eventos \( \{ A_i : i \in I \} \) é independente se
$$
P \left( \bigcap_{i \in J} A_i \right) = \prod_{i \in J} P(A_i)
$$
para todo subconjunto finito \( J \) de \( I \). Se \( A \) e \( B \) não são independentes, escrevemos \( A \not\perp B \).

### Tipos de Independência de Eventos
A independência pode surgir de duas formas distintas:
* Em alguns casos, assumimos explicitamente que dois eventos são independentes (Ex: Achar uma moeda na rua e ganhar na loteria).
* Em outros casos, derivamos a independência a partir de cálculos ou das propriedades do problema.

### Exemplo de Eventos Independentes
Vamos considerar o lançamento de um dado justo. Definimos os seguintes eventos:
* Evento \( A = \{2, 4, 6\} \), ou seja, os resultados em que o dado mostra um número par.
* Evento \( B = \{1, 2, 3, 4\} \), ou seja, os resultados em que o dado mostra um número menor ou igual a 4.

A interseção de \( A \) e \( B \), ou seja, os resultados que pertencem a ambos os eventos \( A \) e \( B \), é dada por:
$$
A \cap B = \{2, 4\}
$$
Estes são os números que são simultaneamente pares e menores ou iguais a 4.

## Probabilidade de \( A \cap B \)
A probabilidade de \( A \cap B \) é dada pelo número de resultados favoráveis (que são 2: \( 2 \) e \( 4 \)) dividido pelo número total de resultados possíveis (6, pois o dado tem 6 faces):
$$
P(A \cap B) = \frac{2}{6} = \frac{1}{3}
$$

Agora, calculamos as probabilidades individuais:
* A probabilidade de \( A \) (resultados pares) é:
$$
P(A) = \frac{3}{6} = \frac{1}{2}
$$
* A probabilidade de \( B \) (resultados menores ou iguais a 4) é:
$$
P(B) = \frac{4}{6} = \frac{2}{3}
$$

### Verificando a Independência
Para que \( A \) e \( B \) sejam independentes, a probabilidade da interseção deve ser igual ao produto das probabilidades individuais:
$$
P(A \cap B) = P(A) \times P(B)
$$
Verificamos:
$$
P(A \cap B) = \frac{1}{3}, \quad P(A) \times P(B) = \frac{1}{2} \times \frac{2}{3} = \frac{1}{3}
$$
Como \( P(A \cap B) = P(A) \times P(B) \), concluímos que os eventos \( A \) e \( B \) são independentes.

``Neste caso, não assumimos que \( A \) e \( B \) são independentes — apenas descobrimos que eram'' significa que, ao calcular as probabilidades e verificar a condição de independência, chegamos à conclusão de que \( A \) e \( B \) são eventos independentes, sem fazer essa suposição previamente.

### Eventos Disjuntos e Independência
Suponha que \( A \) e \( B \) sejam eventos disjuntos, cada um com probabilidade positiva.
Podemos nos perguntar: eles podem ser independentes?

A resposta é não. Isso ocorre porque a probabilidade da interseção de \( A \) e \( B \) é zero:
$$
P(A \cap B) = P(\emptyset) = 0
$$
No entanto, a probabilidade de \( A \) e \( B \) é positiva:
$$
P(A) > 0 \quad \text{e} \quad P(B) > 0
$$
Se fossem independentes, deveríamos ter:
$$
P(A \cap B) = P(A) P(B)
$$
Mas, como \( P(A \cap B) = 0 \), isso não pode ser verdade.

### Independência em Diagrama de Venn
Exceto neste caso especial, não é possível julgar a independência de dois eventos apenas olhando seus conjuntos em um diagrama de Venn.

Um diagrama de Venn é uma representação gráfica dos conjuntos e suas relações, como interseções e uniões. No entanto, em termos de independência, não podemos sempre julgar se dois eventos são independentes apenas olhando para um diagrama de Venn.

### Por que não podemos julgar independência apenas com o Diagrama de Venn?
A independência entre dois eventos \( A \) e \( B \) é uma propriedade que envolve as probabilidades dos eventos e não apenas as suas relações gráficas. Especificamente, para dois eventos serem independentes, deve se cumprir a seguinte condição:
$$
P(A \cap B) = P(A)P(B)
$$
No entanto, em um diagrama de Venn, apenas a visualização das interseções entre os conjuntos \( A \) e \( B \) não fornece informações sobre as probabilidades associadas a esses eventos, o que é crucial para verificar a independência.

### Resumo sobre Independência
* \( A \) e \( B \) são independentes se e somente se \( P(A \cap B) = P(A)P(B) \).
* A independência é, às vezes, assumida e, outras vezes, derivada.
* Eventos disjuntos com probabilidade positiva não são independentes.





## Probabilidade Condicional
Se $P(B) > 0$, então a probabilidade condicional de $A$ dado $B$ é:
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Pense em $P(A|B)$ como a fração de vezes em que $A$ ocorre entre aquelas em que $B$ ocorre.

Para qualquer $B$ fixo tal que $P(B) > 0$, $P(\cdot | B)$ é uma probabilidade, ou seja, ela satisfaz os três axiomas da probabilidade.

### Álgebra $\sigma$ e Espaço de Probabilidade
Geralmente, não é viável atribuir probabilidades a todos os subconjuntos de um espaço amostral $\Omega$. Em vez disso, restringe-se a atenção a um conjunto de eventos chamado álgebra $\sigma$ ou $\sigma$-álgebra, que é uma classe $A$ que satisfaz as seguintes propriedades:

* $\emptyset \in A$, ou seja, o conjunto vazio está em $A$.
* Se $A_1, A_2, \dots \in A$, então $\bigcup_{i=1}^{\infty} A_i \in A$, ou seja, a união contável de eventos em $A$ também está em $A$.
* Se $A \in A$, então $A^c \in A$, ou seja, se $A$ está em $A$, então o complemento de $A$ também está em $A$.

Os conjuntos em $A$ são chamados de conjuntos mensuráveis.

Chamamos o par $(\Omega, A)$ de espaço mensurável. Se $P$ for uma medida de probabilidade definida sobre $A$, então o triplo $(\Omega, A, P)$ é chamado de espaço de probabilidade.

### Axiomas da Probabilidade Condicional
Em particular, temos as seguintes propriedades:
* $P(A|B) \geq 0$, ou seja, a probabilidade condicional é sempre não negativa.
* $P(\Omega|B) = 1$, ou seja, a probabilidade condicional do espaço amostral $\Omega$, dado $B$, é 1.
* Se $A_1, A_2, \dots$ são eventos disjuntos, então:
$$P\left( \bigcup_{i=1}^{\infty} A_i \Big| B \right) = \sum_{i=1}^{\infty} P(A_i | B).$$

No entanto, em geral, não é verdade que:
$$P(A|B \cup C) = P(A|B) + P(A|C).$$
As regras da probabilidade aplicam-se apenas aos eventos à esquerda da barra $|$.
$$P(A|B) \neq P(B|A)$$

#### Exemplo de Probabilidade Condicional
Um teste médico para a doença $D$ tem os resultados $+$ e $-$. As probabilidades são as seguintes:

|   | D     | D^c   |
|---|-------|-------|
| + | 0.009 | 0.099 |
| - | 0.001 | 0.891 |

#### Cálculo de Probabilidades Condicionais
Da definição de probabilidade condicional, temos:
$$P(+|D) = \frac{P(+ \cap D)}{P(D)} = \frac{0.009}{0.009 + 0.001} = 0.9$$
e
$$P(-|D^c) = \frac{P(- \cap D^c)}{P(D^c)} = \frac{0.891}{0.891 + 0.099} \approx 0.9.$$
Aparentemente, o teste é bastante preciso: pessoas doentes resultam positivo 90\% das vezes e pessoas saudáveis resultam negativo cerca de 90\% das vezes.

Suponha que você faça o teste e o resultado seja positivo. Qual é a probabilidade de você ter a doença?

A maioria das pessoas responderia 0.90. No entanto, a resposta correta é:
$$P(D|+) = \frac{P(+ \cap D)}{P(+)} = \frac{0.009}{0.009 + 0.099} \approx 0.08.$$
A lição aqui é que é necessário calcular a resposta numericamente. Não confie apenas na sua intuição.

## Teorema de Bayes

**Teorema (Lei de Probabilidade Total).**
Seja $A_1, \dots, A_k$ uma partição de $\Omega$.
Então, para cada evento $B$,
$$
P(B) = \sum_{i=1}^k P(B|A_i)P(A_i).
$$
*Obs: Veja prova na página 12.

**Teorema (Teorema de Bayes).**
Seja $A\_1, \dots, A\_k$ uma partição de $\Omega$ tal que $P(A\_i) > 0$ para cada $i$
Se $P(B) > 0$ então, para cada $i = 1, \dots, k$,
$$
P(A_i|B) = \frac{P(B|A_i)P(A_i)}{\sum_j P(B|A_j)P(A_j)}.
$$

### Exercício 1

Steve é ​​muito tímido e retraído, invariavelmente prestativo, mas com muito pouco interesse pelas pessoas ou pelo mundo da realidade. De alma mansa e organizada, ele tem necessidade de ordem e estrutura e paixão pelos detalhes.  
**Qual é a probabilidade de Steve ser bibliotecário e não agricultor?**

*Obs: Veja mais exemplos na página 12, crédito para 3blue1brown.

### Exercício 2

Suponha que 30% dos proprietários de computadores usem um Macintosh, 50%
usam Windows e 20% usam Linux. Suponha que 65 por cento de
os usuários de Mac sucumbiram a um vírus de computador, 82% dos
Os usuários do Windows pegam o vírus e 50% dos usuários do Linux pegam
o vírus. Selecionamos uma pessoa aleatoriamente e descobrimos que seu sistema era
infectado com o vírus. **Qual é a probabilidade de ela ser usuária do Windows?**
*Obs: Ex 19, pág. 16