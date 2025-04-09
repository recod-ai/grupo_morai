---
title: Variáveis Aleatórias
weight: 2
---

## Variáveis Aleatórias

### Introdução
A estatística e a mineração de dados estão preocupadas com dados. Como vinculamos espaços amostrais e eventos aos dados? O vínculo é fornecido pelo conceito de uma variável aleatória.



#### O que é uma variável aleatória?
> Definição 2.1
> Uma **variável aleatória** $ X $ é um mapeamento $ X: \Omega \rightarrow \mathbb{R} $
> que atribui um número real $ X(\omega) $ a cada resultado $ \omega $.


-  $ X $ representa a variável aleatória.
-  $ \Omega $ é o espaço amostral que contém todos os resultados possíveis de um experimento aleatório.
-  $ \mathbb{R} $ é o conjunto dos números reais.

A expressão indica que para cada resultado $ \omega $ no espaço amostral $ \Omega $, a variável aleatória $ X $ atribui um valor real $ X(\omega) $.

#### Exemplo de Variável Aleatória Discreta
**Exemplo 2.2.** Lançar uma moeda dez vezes. Seja $ X(\omega) $ o número de caras (H) na sequência $ \omega $. Por exemplo, se $ \omega = $ HHTHHTHHTT, então $ X(\omega) = 6 $.
\bigskip

-  Espaço amostral $ \Omega $: todas as sequências possíveis de 10 lançamentos de moeda.
-  $ X $ transforma cada sequência em um número (contagem de caras).


#### Exemplo de Variável Aleatória Contínua
**Exemplo 2.3.** Seja $ \Omega = \{(x, y): x^2 + y^2 \leq 1\} $ o disco unitário. Considere
a escolha de um ponto ao acaso em $ \Omega $. Um resultado típico é da forma $ \omega = (x, y) $. Alguns exemplos de variáveis aleatórias são:

-  $ X(\omega) = x $ 
-  $ Z(\omega) = x + y $
-  $ Y(\omega) = y $ 
-  $ W(\omega) = \sqrt{x^2 + y^2} $

> Definição de evento através de $ X $
> Dada uma variável aleatória $ X $ e um subconjunto $ A $ dos números reais, definimos $ X^{-1}(A) = \{\omega \in \Omega : X(\omega) \in A\} $ e deixamos:
> $$ P(X \in A) = P(X^{-1}(A)) = P(\{\omega \in \Omega: X(\omega) \in A\}) $$
> $$ P(X = x) = P(X^{-1}(x)) = P(\{\omega \in \Omega: X(\omega) = x\}) $$


#### Distribuição de uma Variável Aleatória Discreta
**Exemplo 2.4.** Lançar uma moeda duas vezes e seja $ X $ o número de caras (H). Então:

| $\omega$ |  $P(\{\omega\})$ | $X(\omega)$ |
| --- | ---| ---| 
| TT | 1/4 | 0 |
| TH | 1/4 | 1 |
| HT | 1/4 | 1 |
| HH | 1/4 | 2 |

-  $ P(X = 0) = P(\{TT\}) = \frac{1}{4} $
-  $ P(X = 1) = P(\{TH, HT\}) = \frac{1}{2} $
-  $ P(X = 2) = P(\{HH\}) = \frac{1}{4} $


##### Conceitos Fundamentais

-  **Espaço Amostral** ($\Omega$): Conjunto de todos os resultados possíveis de um experimento aleatório.
-  **Variável Aleatória** ($X$): Função que associa cada resultado do espaço amostral a um número real.
-  **Distribuição de Probabilidade**: Descreve como as probabilidades estão distribuídas sobre os valores da variável aleatória.


### Funções de Distribuição e Funções de Probabilidade
#### Função de Distribuição
> Definição 2.5
> A **Função de Distribuição Acumulada** (CDF - Cumulative Distribution Function) $ F_X $ de uma variável aleatória $ X $ é a função $ F_X: \mathbb{R} \rightarrow [0, 1] $ definida por:
> $$ F_X(x) = P(X \leq x). $$


#### Função de Distribuição
> Definição 2.5
> A **Função de Distribuição Acumulada** (CDF - Cumulative Distribution Function) $ F_X $ de uma variável aleatória $ X $ é a função $ F_X: \mathbb{R} \rightarrow [0, 1] $ definida por:
> $$ F_X(x) = P(X \leq x). $$

$ F_X(x) $ representa a acumulação da probabilidade de todos os valores da variável aleatória $ X $ que são menores ou iguais a um dado valor $ x $. Isso significa que, para qualquer número real $ x $, $ F_X(x) $ irá fornecer a probabilidade total de $ X $ estar no intervalo de $ -\infty $ até $ x $, o que resulta em um valor entre 0 e 1.

#### Exemplo de CDF para uma Variável Aleatória Discreta   
**Exemplo 2.6.** Lançar uma moeda justa duas vezes e seja $ X $ o número de caras. Então:
$$ P(X = 0) = P(X = 2) = \frac{1}{4} \quad \text{e} \quad P(X = 1) = \frac{1}{2}. $$
A função de distribuição $ F_X(x) $ é:
$$ F_X(x) = \begin{cases}
0 & \text{se } x < 0 \\
\frac{1}{4} & \text{se } 0 \leq x < 1 \\
\frac{3}{4} & \text{se } 1 \leq x < 2 \\
1 & \text{se } x \geq 2.
\end{cases} $$

-  A CDF $ F_X $ é contínua à direita e não-decrescente.


#### Exemplo de CDF para uma Variável Aleatória Discreta   
\begin{figure}
\centering
\includegraphics[width=0.8\textwidth]{Apresentação-2/functions_1.png} \caption{CDF para o lançamento de uma moeda duas vezes (Exemplo 2.6).}
\end{figure}

#### Teoremas sobre CDF
> Teorema 2.7
> Se $ X $ tem CDF $ F $ e se $ Y $ tem CDF $ G $, e se $ F(x) = G(x) $ para todo $ x $, então $ P(X \in A) = P(Y \in A) $ para todo conjunto $ A $.

Esse teorema estabelece que se duas variáveis aleatórias, $ X $ e $ Y $, possuem funções de distribuição acumulada (CDF) idênticas — ou seja, $ F(x) = G(x) $ para todo $ x $ real —, então as probabilidades de $ X $ e $ Y $ pertencerem a qualquer conjunto $ A $ também serão iguais.

#### Teoremas sobre CDF
> Teorema 2.8
> Uma função $ F $ é a CDF de uma variável aleatória $ X $ se, e somente se, $ F $ satisfaz as seguintes três condições:
> 
> - (i) $ F $ é não-decrescente: $ x_1 < x_2 $ implica que $ F(x_1) \leq F(x_2) $.
> - (ii) $ F $ é normalizada: $ \lim_{x \to -\infty} F(x) = 0 $ e $ \lim_{x \to \infty} F(x) = 1 $.
> - (iii) $ F $ é contínua à direita: $ F(x) = F(x^+) $ para todo $ x $, onde $ F(x^+) = \lim_{y \to x, y > x} F(y) $.
> 


#### Variáveis Aleatórias Discretas e PMF
> Definição 2.9
> $ X $ é **discreta** se assume um número enumerável de valores $ \{x_1, x_2, \ldots\} $. A **Função de Massa de Probabilidade** (PMF - Probability Mass Function) para $ X $ é definida por:
> $$ f_X(x) = P(X = x). $$


-  $ f_X(x) \geq 0 $ para todo $ x \in \mathbb{R} $.
-  $ \sum_i f_X(x_i) = 1 $.
-  A relação entre a PMF e a CDF é: $ F_X(x) = P(X \leq x) = \sum_{x_i \leq x} f_X(x_i) $.


#### Exemplo de PMF
**Exemplo 2.10.** A função de massa de probabilidade para o Exemplo 2.6 é:
$$ f_X(x) = \begin{cases}
\frac{1}{4} & \text{se } x = 0 \\
\frac{1}{2} & \text{se } x = 1 \\
\frac{1}{4} & \text{se } x = 2 \\
0 & \text{caso contrário}.
\end{cases} $$

#### Exemplo de PMF
\begin{figure}
\centering
\includegraphics[width=0.8\textwidth]{Apresentação-2/functions_2.png} \caption{Função de probabilidade para o lançamento de uma moeda duas vezes (Exemplo 2.6).}
\end{figure}

#### Variáveis Aleatórias Contínuas e PDF
> Definição 2.11
> Uma **variável aleatória $ X $** é **contínua** se existe uma função $ f_X $ tal que:
> 
> -  $ f_X(x) \geq 0 $ para todo $ x $,
> -  $ \int_{-\infty}^{\infty} f_X(x)dx = 1 $,
> -  Para todo $ a \leq b $, $ P(a < X < b) = \int_{a}^{b} f_X(x)dx $.
> 
> A função $ f_X $ é chamada de **Função de Densidade de Probabilidade** (PDF).


#### Relação entre PDF e CDF
> 
> A CDF $ F_X(x) $ está relacionada à PDF $ f_X(x) $ por:
> $$ F_X(x) = \int_{-\infty}^{x} f_X(t)dt $$
> e $ f_X(x) = F_X'(x) $ em todos os pontos $ x $ nos quais $ F_X $ é diferenciável.


#### Exemplos de PDF e CDF
Exemplo 2.12: 
A variável $ X $ tem PDF:
$$ f_X(x) = \begin{cases}
1 & \text{se } 0 \leq x \leq 1 \\
0 & \text{caso contrário}
\end{cases} $$
Podemos verificar que essa é uma PDF válida, pois sua integral total deve ser 1:
$$
\int_{0}^{1} 1 \, dx = x \Big|_0^1 = 1 - 0 = 1.
$$

#### Exemplos de PDF e CDF
Agora, calculamos a CDF $ F_X(x) $, definida como:
$$
F_X(x) = P(X \leq x) = \int_{-\infty}^{x} f_X(t) \, dt.
$$

#### Exemplos de PDF e CDF

-  Para $ x < 0 $, como $ f_X(x) = 0 $ para esses valores:
$$
F_X(x) = \int_{-\infty}^{x} 0 \, dt = 0.
$$  
-  Para $ 0 \leq x \leq 1 $:
$$
F_X(x) = \int_{0}^{x} 1 \, dt = x.
$$
-  Para $ x > 1 $:
$$
F_X(x) = \int_{0}^{1} 1 \, dt = 1.
$$


#### Exemplos de PDF e CDF
Portanto, a CDF $ F_X(x) $ é:
$$ F_X(x) = \begin{cases}
0 & x < 0 \\
x & 0 \leq x \leq 1 \\
1 & x > 1
\end{cases} $$

#### Exemplos de PDF e CDF
\begin{figure}
\centering
\includegraphics[width=0.5\textwidth]{Apresentação-2/functions_3.png} \caption{CDF para a distribuição Uniforme (0,1).}
\end{figure}

#### Exemplos de PDF e CDF
Exemplo 2.13
Suponha que $ X $ tem PDF:
$$ f(x) = \begin{cases}
0 & x < 0 \\
\frac{1}{(1+x)^2} & x \geq 0
\end{cases} $$
Esta é uma PDF bem definida, pois $ \int f(x)dx = 1 $.

#### Variáveis Contínuas
> **Aviso** Para variáveis aleatórias contínuas, $ P(X = x) = 0 $ para todo $ x $. A PDF $ f(x) $ não deve ser interpretada como $ P(X = x)$. Probabilidades são obtidas pela integração da PDF.

-  A PDF pode ser maior que 1 em alguns pontos.
-  A PDF pode ser não limitada.


#### Variáveis Contínuas
Exemplo 2.14: 
A função:
$$ f(x) = \begin{cases}
0 & x < 0 \\
\frac{1}{1+x} & x \geq 0
\end{cases} $$
não é uma PDF, pois $ \int f(x)dx = \infty $.

#### Lema da CDF
>  Lema 2.15
> Seja $ F $ a CDF de uma variável aleatória $ X $. Então:
> -  $ P(X = x) = F(x) - F(x-) $ onde $ F(x-) = \lim_{y \uparrow x} F(y) $;
> -  $ P(x < X \leq y) = F(y) - F(x) $;
> -  $ P(X > x) = 1 - F(x) $;
> -  Se $ X $ é contínua, então $ F(b) - F(a) = P(a < X < b) = P(a \leq X < b) = P(a < X \leq b) = P(a \leq X \leq b) $.


#### Lema 2.15
> 
> $ P(X = x) = F(x) - F(x-) $ onde $ F(x-) = \lim_{y \uparrow x} F(y) $

Exemplo: Seja $ X $ o número de lançamentos até obter cara em um jogo de moeda (distribuição geométrica). A CDF terá saltos em valores inteiros, e a diferença $ F(x) - F(x-) $ dará a probabilidade de $ X = x $.

#### Lema 2.15
> 
> $ P(x < X \leq y) = F(y) - F(x) $

Exemplo: Se $ X $ for o tempo de espera por um ônibus, modelado por uma distribuição exponencial, então a probabilidade de o ônibus chegar entre 5 e 10 minutos é:
$$
P(5 < X \leq 10) = F(10) - F(5).
$$

#### Lema 2.15
> 
> $ P(X > x) = 1 - F(x) $

Exemplo: \\
Se $ X $ representa a vida útil de um componente eletrônico, a probabilidade de durar mais que 1000 horas é:
$$
P(X > 1000) = 1 - F(1000).
$$

#### Lema 2.15
> 
> Se $ X $ é contínua, então $ F(b) - F(a) = P(a < X < b) = P(a \leq X < b) = P(a < X \leq b) = P(a \leq X \leq b) $

Exemplo: \\
Se $X $ segue uma distribuição normal ($ X \sim \mathcal{N}(\mu, \sigma^2) $), a probabilidade de $ X $ estar entre 1 e 2 é:
$$
P(1 < X < 2) = F(2) - F(1).
$$
Como $ X $ é contínua, os diferentes intervalos resultam na mesma probabilidade (independente se os extremos estão incluídos ou não).

#### Função da CDF
> Definição 2.16
> A **função inversa da CDF** ou **função quantílica** $ F^{-1}(q) $ é definida por:
> $$ F^{-1}(q) = \inf\{x : F(x) > q\} $$
> para $ q \in [0, 1] $. Se $ F $ é estritamente crescente e contínua, $ F^{-1}(q) $ é o número real único $ x $ tal que $ F(x) = q $.


-  $ F^{-1}(1/4) $ é o primeiro quartil.
-  $ F^{-1}(1/2) $ é a mediana (ou segundo quartil).
-  $ F^{-1}(3/4) $ é o terceiro quartil.


#### Igualdade em Distribuição
Duas variáveis aleatórias $ X $ e $ Y $ são **iguais em distribuição** — escrito $ X \overset{d}{=} Y $ — se $ F_X(x) = F_Y(x) $ para todo $ x $.
> Observações
> Igualdade em distribuição não significa que $ X $ e $ Y $ sejam iguais como funções. Por exemplo, se $ P(X = 1) = P(X = -1) = 1/2 $ e $ Y = -X $, então $ X \overset{d}{=} Y $ mas $ X \neq Y $.


#### Igualdade em Distribuição ($ X \overset{d}{=}Y $)
> **Exemplo**
> Seja $ X $ uma variável aleatória tal que:
> $$
> P(X = 1) = \frac{1}{2}, \quad P(X = -1) = \frac{1}{2}.
> $$
> Definimos $ Y $ como $ Y = -X $. Então:
> $$
> P(Y = 1) = P(X = -1) = \frac{1}{2}, \quad P(Y = -1) = P(X = 1) = \frac{1}{2}.
> $$
> Assim, $ X $ e $ Y $ possuem a mesma distribuição, ou seja:
> $$
> X \overset{d}{=} Y, \quad \text{mas } X \neq Y.
>$$

### Algumas Variáveis Aleatórias Discretas Importantes
#### Aviso sobre Notação!
É tradicional escrever $ X \sim F $ para indicar que $ X $ tem distribuição $ F $. **Essa notação é infeliz**, pois o símbolo $ \sim $ também é usado para denotar uma aproximação. A notação $ X \sim F $ é tão difundida que estamos "presos" a ela. Leia $ X \sim F $ como "$ X $ tem distribuição $ F $" e **não** como "$ X $ é aproximadamente $ F $".

#### Distribuição de Massa Pontual (Point Mass Distribution)
Dizemos que $ X $ tem uma **distribuição de massa pontual** em $ a $, denotada por $ X \sim \delta_a $, se:
$$
P(X = a) = 1.
$$
A **função de distribuição acumulada (CDF)** é:
$$
F(x) = 
\begin{cases} 
0 & \text{se } x < a, \\
1 & \text{se } x \geq a.
\end{cases}
$$
A **função de massa de probabilidade (PMF)** é:
$$
f(x) = 
\begin{cases} 
1 & \text{se } x = a, \\
0 & \text{caso contrário}.
\end{cases}
$$

#### Exemplo: Tempo de resposta de um sistema determinístico
Se um sistema computacional sempre responde em exatamente $5 \text{ ms}$, sem variação, então o tempo de resposta $ X $ segue uma distribuição de massa pontual em 5:
$$
X \sim \delta_5
$$
Isso significa que $ P(X = 5) = 1 $, e o sistema **nunca** apresenta outro tempo de resposta.

#### Distribuição Uniforme Discreta (Discrete Uniform Distribution)
Seja $ k > 1 $ um inteiro dado. Suponha que $ X $ tem **função de massa de probabilidade** dada por:
$$
f(x) = 
\begin{cases} 
\frac{1}{k} & \text{para } x = 1, 2, \dots, k, \\
0 & \text{caso contrário}.
\end{cases}
$$
Dizemos que $ X $ tem uma **distribuição uniforme discreta** no conjunto $ \{1, 2, \dots, k\} $.

#### Exemplo: Lançamento de um dado justo
Considere o lançamento de um dado de seis faces. Cada face tem a mesma probabilidade de ocorrer, ou seja, a variável aleatória $ X $, que representa o valor obtido no lançamento, segue uma distribuição uniforme discreta:
$$
X \sim \text{Unif}(\{1, 2, 3, 4, 5, 6\})
$$
A função de massa de probabilidade (PMF) é:
$$
f(x) =
\begin{cases} 
\frac{1}{6}, & x \in \{1, 2, 3, 4, 5, 6\} \\
0, & \text{caso contrário}
\end{cases}
$$
Isso significa que a probabilidade de obter qualquer número entre 1 e 6 é $ \frac{1}{6} $.

#### **A Distribuição de Bernoulli**
A **Distribuição de Bernoulli** modela experimentos com apenas dois possíveis resultados: **sucesso** ($ X = 1 $) ou **fracasso** ($ X = 0 $). Essa distribuição é fundamental em experimentos binários, como o lançamento de uma moeda ou o funcionamento de um componente eletrônico.

Seja $ X $ uma variável aleatória de Bernoulli com parâmetro $ p $, onde $ p $ representa a probabilidade de sucesso. A notação usada é:
$$
X \sim \text{Bernoulli}(p)
$$

#### **A Distribuição de Bernoulli: PMF**    
A **função de massa de probabilidade (PMF)** para $ X $ é dada por:
$$
f(x) = p^x (1 - p)^{1 - x} \quad \text{para } x \in \{0, 1\}.
$$

Isso significa que:
$$
P(X = 1) = p \quad \text{e} \quad P(X = 0) = 1 - p
$$
para algum $ p \in [0, 1] $. Em outras palavras, a probabilidade de $ X $ ser 1 (sucesso) é $ p $, e a probabilidade de ser 0 (fracasso) é $ 1 - p $.

#### Distribuição Binomial (Binomial Distribution)
Suponha que temos uma moeda que cai "cara" com probabilidade $ p $, onde $ 0 \leq p \leq 1 $. Lançamos a moeda $ n $ vezes e seja $ X $ o número de ``caras". Assumindo que os lançamentos são independentes, a **função de massa de probabilidade** é:
$$
f(x) = 
\begin{cases} 
\binom{n}{x} p^x (1 - p)^{n - x} & \text{para } x = 0, 1, \dots, n, \\
0 & \text{caso contrário}.
\end{cases}
$$
Uma variável aleatória com essa função de massa é chamada de **variável aleatória binomial**, e escrevemos $ X \sim \text{Binomial}(n, p) $.

#### **Propriedade da Distribuição Binomial**
Se $ X_1 \sim \text{Binomial}(n_1, p) $ e $ X_2 \sim \text{Binomial}(n_2, p) $, então a soma $ X_1 + X_2 $ segue uma distribuição binomial com parâmetros $ n_1 + n_2 $ e $ p $. Ou seja:
$$
X_1 + X_2 \sim \text{Binomial}(n_1 + n_2, p).
$$

#### **Explicação e Exemplo**
**Explicação:**

-  $ X_1 $ e $ X_2 $ são duas variáveis aleatórias independentes, ambas seguindo distribuições binomiais com parâmetros $ n_1 $, $ p $ e $ n_2 $, $ p $, respectivamente.
-  $ X_1 $ representa o número de sucessos em $ n_1 $ tentativas independentes, e $ X_2 $ representa o número de sucessos em $ n_2 $ tentativas independentes, ambas com a mesma probabilidade de sucesso $ p $.

Assim, a soma $ X_1 + X_2 $ tem uma PMF dada por:
$$
P(X_1 + X_2 = x) = \binom{n_1 + n_2}{x} p^x (1 - p)^{n_1 + n_2 - x}.
$$

#### Aviso!
Não confunda:

-  $ X $: variável aleatória.
-  $ x $: valor específico da variável aleatória.
-  $ n $ e $ p $: parâmetros (números reais fixos). O parâmetro $ p $ é geralmente desconhecido e deve ser estimado a partir dos dados.


#### **Distribuição Geométrica (Geometric Distribution)**
Dizemos que $ X $ tem uma **distribuição geométrica** com parâmetro $ p \in (0, 1) $, denotada por $ X \sim \text{Geom}(p) $, se:
$$
P(X = k) = p(1 - p)^{k - 1}, \quad \text{para } k \geq 1.
$$
Essa distribuição modela o número de tentativas até o primeiro sucesso em uma sequência de ensaios de Bernoulli independentes.

**Exemplo Prático:**
Considere uma moeda com $ p = 0.3 $ para obter cara. A distribuição geométrica modela o número de lançamentos até obter a primeira cara.

#### Resumo das Distribuições

-  **Massa Pontual ($ \delta_a $)**: Probabilidade concentrada em um único ponto $ a $.
-  **Uniforme Discreta**: Probabilidade igualmente distribuída entre $ k $ valores.
-  **Bernoulli**: Modela um experimento binário (sucesso/fracasso).
-  **Binomial**: Conta o número de sucessos em $ n $ ensaios de Bernoulli.
-  **Geométrica**: Conta o número de tentativas até o primeiro sucesso.


### Algumas Variáveis Aleatórias Continuas Importantes
#### Distribuição Uniforme (Uniform Distribution)
Dizemos que $ X $ tem uma **distribuição uniforme** no intervalo $[a, b]$, denotada por $ X \sim \text{Uniform}(a, b) $, se sua função densidade de probabilidade (PDF) é:
$$
f(x) = 
\begin{cases} 
\frac{1}{b - a} & \text{para } x \in [a, b], \\
0 & \text{caso contrário}.
\end{cases}
$$
A **função de distribuição acumulada (CDF)** é:
$$
F(x) = 
\begin{cases} 
0 & \text{se } x < a, \\
\frac{x - a}{b - a} & \text{se } x \in [a, b], \\
1 & \text{se } x > b.
\end{cases}
$$

#### Distribuição Normal (Gaussiana)
Dizemos que $ X $ tem uma **distribuição normal** (ou Gaussiana) com parâmetros $\mu$ e $\sigma$, denotada por $ X \sim N(\mu, \sigma^2) $, se sua função densidade de probabilidade (PDF) é:
$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left\{ -\frac{1}{2\sigma^2} (x - \mu)^2 \right\}, \quad x \in \mathbb{R},
$$
onde $\mu \in \mathbb{R}$ é a média e $\sigma > 0$ é o desvio padrão.

#### Propriedades da Distribuição Normal

-  A distribuição normal é simétrica em torno da média $\mu$.
-  A área sob a curva da PDF é sempre igual a 1.
-  A distribuição normal é amplamente utilizada na natureza e em estatística devido ao **Teorema Central do Limite**.


#### Distribuição Normal Padrão
Se $\mu = 0$ e $\sigma = 1$, dizemos que $ X $ tem uma **distribuição normal padrão**, denotada por $ Z \sim N(0, 1) $. Sua PDF e CDF são denotadas por:
$$
\phi(z) = \frac{1}{\sqrt{2\pi}} \exp\left\{ -\frac{z^2}{2} \right\}, \quad \Phi(z) = \int_{-\infty}^z \phi(t) \, dt.
$$
Não há uma fórmula fechada para $\Phi(z)$, mas tabelas e softwares estatísticos podem ser usados para calcular probabilidades.

#### **Transformações da Distribuição Normal**
Vamos discutir três importantes transformações da distribuição normal:

-  **Padronização de uma variável normal:**
Se $ X \sim N(\mu, \sigma^2) $, ou seja, $ X $ segue uma distribuição normal com média $ \mu $ e variância $ \sigma^2 $, então a variável $ Z $ definida por
$$
Z = \frac{X - \mu}{\sigma}
$$
segue uma distribuição normal padrão, ou seja, $ Z \sim N(0, 1) $. A transformação $ Z $ é conhecida como a padronização de $ X $, e a distribuição de $ Z $ tem média 0 e variância 1. Isso é útil quando queremos comparar variáveis com diferentes médias e desvios padrão em uma escala comum.


#### **Transformações da Distribuição Normal (continuação)**

-  **Transformação inversa:**
Se $ Z \sim N(0, 1) $, ou seja, $ Z $ é uma variável aleatória com distribuição normal padrão, então a transformação
$$
X = \mu + \sigma Z
$$
resulta em uma variável $ X $ que segue uma distribuição normal com média $ \mu $ e variância $ \sigma^2 $, ou seja, $ X \sim N(\mu, \sigma^2) $. Esta transformação é útil para gerar uma variável normal com qualquer média e desvio padrão a partir da distribuição normal padrão.


#### **Transformações da Distribuição Normal (continuação)**  

-  **Soma de variáveis normais independentes:**
Se $ X_i \sim N(\mu_i, \sigma_i^2) $ para $ i = 1, 2, \dots, n $, e as variáveis $ X_1, X_2, \dots, X_n $ são independentes, então a soma dessas variáveis segue uma distribuição normal com média e variância dadas por:
$$
\sum_{i=1}^n X_i \sim N\left( \sum_{i=1}^n \mu_i, \sum_{i=1}^n \sigma_i^2 \right).
$$
Ou seja, a soma de variáveis normais independentes é novamente uma variável normal, com a média sendo a soma das médias e a variância sendo a soma das variâncias das variáveis originais. Isso é particularmente útil em modelos de agregação de dados, como na teoria dos erros em experimentos.


#### Cálculo de Probabilidades
Para $ X \sim N(\mu, \sigma^2) $, a probabilidade $ P(a < X < b) $ é dada por:
$$
P(a < X < b) = P\left( \frac{a - \mu}{\sigma} < Z < \frac{b - \mu}{\sigma} \right) = \Phi\left( \frac{b - \mu}{\sigma} \right) - \Phi\left( \frac{a - \mu}{\sigma} \right).
$$
Isso permite calcular probabilidades usando a CDF da distribuição normal padrão ($\Phi$).

#### Importância da Distribuição Normal

-  A distribuição normal é fundamental em estatística e probabilidade.
-  Muitos fenômenos naturais seguem uma distribuição aproximadamente normal.
-  O **Teorema Central do Limite** afirma que a soma de muitas variáveis aleatórias independentes tende a uma distribuição normal.


