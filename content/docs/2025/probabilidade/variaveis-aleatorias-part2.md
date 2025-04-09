---
title: Variáveis Aleatórias (p2)
weight: 3
---

Esta apresentação abordará a segunda parte do Capítulo 2 de All of Statistics: A Concise Course in Statistical Inference.

### Relembrando
#### Variável Aleatória
> Variável Aleatória
> Uma variável aleatória é um mapeamento $X : \Omega \to  E$ que para cada resultado $\omega$, existe um número real relacionado $X(\omega)$.

> Probabilidade de uma V.A.
> $$
> P(X \in S) = P(\{\omega \in \Omega \mid X(\omega) \in S\})
> $$


#### Definições de Funções com $X$ discreto
> Função de Massa de Probabilidade (PMF)
> $$
> \begin{split}
> &\quad \quad \quad f_X(x) = P(X = x)
> \end{split}
> $$

> Função de Distribuição Acumulada (CDF)
> $$
> F_X(x) = P(X \leq x) = \sum_{z = -\infty}^x f_X(z)
> $$


#### Definições de Funções com $X$ contínuo
> Função de Distribuição Acumulada (CDF)
> $$
> F_X(x) = P(X \leq x) = \int_{-\infty}^x f_X(z)dz
> $$

> Função de Densidade de Probabilidade (PDF)
> $$
> f_X(x) = F'_X(x)
> $$
> 

### Distribuições Multivariadas

Anteriormente, estudamos variáveis aleatórias que representam um único número, como, por exemplo, o número de um dado sorteado. Porém, é interessante considerar o caso onde temos diversos números aleatórios, como em um lançamento de dois dados. 

#### 
Sejam $X$ e $Y$ duas V.A. discretas, a **PMF conjunta** é dada for $f_{X,Y}(x, y) =P(X =x \text{ e } Y = y)$.
Caso $X, Y$ sejam contínuas, a **PDF conjunta** deve satisfazer:

-  $f(x, y) \geq 0$ para todo $(x, y)$
-  $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) dx dy = 1$
-  para todo $A \subset \mathbb R \times \mathbb R, P((X, Y) \in A) = \int \int_A f(x, y) dx dy$


#### 
Essas definições podem ser generalizadas quando consideramos mais de 2 variáveis aleatórias $X = (X_1, X_2, \dots, X_n)$. Por exemplo, no caso discreto, a PMF conjunta é dada for $f_X(x_1, \dots, x_n) = P(X_1 = x_1 \text{ e } X_2 = x_2 \text{ e } \dots X_n = x_n)$.

#### Exemplo
Imagine o cenário onde temos uma urna com bolas de $k$ cores diferentes. Retiramos $n$ bolas dessa urna (com reposição) e contabilizamos quantas bolas foram retiradas de cada cor. Seja $X_i$ a quantidade de bolas retiradas da $i-$ésima cor. $X = (X_1, \dots, X_n)$ possui uma distribuição **multinomial** com parâmetros $n$ e $p$, onde $p$ é o vetor de probabilidades, e $p_i$ representa a probabilidade de sortear uma bola da $i$-ésima cor.
$$
f_X(x) = \dfrac{n!}{x_1! \cdots x_k!}(p_1^{x_1}\dots p_k^{x_k})
$$

### Distribuição Marginal
#### Definição
> 
> Se $(X, Y)$ discretos possuem distribuição conjunta com PMF $f_{X, Y}$, então a **PMF marginal** de $X$ é definida por:
> $$
> f_X(x) = P(X= x) = \sum_y f_{X,Y}(x, y)
> $$

Essa definição é útil quando desejamos obter a distribuição específica de uma variável aleatória a partir da distribuição conjunta. 

#### Definição
> 
> Se $(X, Y)$ contínuos possuem distribuição conjunta com PDF $f_{X, Y}$, então a **PDF marginal** de $X$ é definida por:
> $$
> f_X(x) =\int f_{X,Y}(x, y)dy
> $$

Essa definição é útil quando desejamos obter a distribuição específica de uma variável aleatória a partir da distribuição conjunta. 

#### Exemplo
Voltando para o exemplo anterior da multinomial. Qual é a distribuição marginal de $X_i$? Nesse caso específico, conseguimos identificar sem a necessidade de resolver o somatório:
$$
f_{X_i}(x_i) = \underbrace{\sum_{x_1=1}^n \sum_{x_2=1}^n \dots \sum_{x_k=1}^n}_{\text{sem o somatório para } i}\dfrac{n!}{x_1! \cdots x_k!}(p_1^{x_1}\dots p_k^{x_k})
$$



-  Vamos considerar que as bolas da cor $i$ são um ``sucesso''
-  As bolas de cores diferentes são um ``fracasso''
-  O número de sucessos é exatamente o que modelamos com uma variável de distribuição **binomial** com parâmetros $n$ e $p_i$.
-  Logo, a PMF marginal de $X_i \sim Bin(n, p_i)$


### Distribuição Condicional
#### Definição
> 
> Sejam $(X, Y)$ duas V.A. discretas. A função de massa de probabilidade condicional de $X$ dado $Y$ é:
> $$
> f_{X \mid Y} (x \mid y)  = P(X =x \mid Y =y) = \dfrac{P(X = x, Y = y)}{P(Y =y)} = \dfrac{f_{X, Y}(x, y)}{f_Y(y)}
> $$
> Se $f_Y(y) > 0$.

Observe que essa definição exige o conhecimento da distribuição marginal $f_Y$. A definição para o caso contínuo é a mesma, porém temos que $f_{X\mid Y}(x \mid y)$ é a função de densidade condicional. 
\scriptsize{Vamos ignorar o detalhe em que $P(Y = y) = 0$ se $Y$ for uma variável contínua. Uma maneira de lidar com isso é considerar a probabilidade de $P(|Y - y | \leq \epsilon)$ quando $\epsilon \to 0$.}

### Transformações de Variáveis Aleatórias

Seja $Y$ definida através de uma função de outra variável aleatória $X$, $Y = r(X)$, como, por exemplo $Y = X^2$. Como calculamos a função de massa de probabilidade de $Y$? Caso $X$ seja uma variável discreta, isso é simples. 
Considere o seguinte exemplo em que $X$ assume valores $-1, 0, 1$ de maneira uniforme e $Y = X^2$. Qual a probabilidade de $Y$ ser $1$?


$X \in \{-1, 0, 1\}, Y = X^2$

-  Se $X = -1 \implies Y = 1$, o que acontece com prob. $\dfrac{1}{3}$
-  Se $X = 0 \implies Y = 0$, o que acontece com prob. $\dfrac{1}{3}$
-  Se $X = 1 \implies Y = 1$, o que acontece com prob. $\dfrac{1}{3}$

Logo, $P(Y = 1) = P(X = -1) + P(X = 1) = \dfrac{2}{3}$.
Se $X$ é discreto, é válida a propriedade:
$$
f_Y(y) = P(Y = y)  = P(r(X) = y) = P(\{x; r(x) = y\}) = P(X \in r^{-1}(y))
$$


Quando $X$ é contínuo, estamos interessados na PDF de $Y$. Se $r$ possui inversa, isto é, $r$ é uma função monótona estritamente crescente ou decrescente, temos:
$$
f_Y(Y) = f_X(r^{-1}(y)) \left| \dfrac{dr^{-1}(y)}{dy}\right|
$$

#### 
Quando $r$ não possui uma função inversa, obtemos $f_Y$ da seguinte forma:

-  Para cada $y$, encontre $A_y = \{ x : r(x) \leq y\}$
-  Encontre a CDF:
$$
F_Y(y) = P(Y \leq y) = \int_{A_y} f_X(x)dx
$$
-  Derive a CDF para obter a PDF: $f_Y(y) = F'_Y(y)$


#### Exemplo

-  Seja $X$ uma V.A. exponencial com parâmetro $1$
-  $f_X(x) = e^{-x}, x>0$ e $F_X(x)  = 1-e^{-x}$
-  $Y = \log X$ (note que o log é invertível)
-  Vamos tentar resolver através dos passos apresentados anteriormente:


#### Exemplo

-  $A_y = \{ x : x \leq e^y\} $
-  Então
$$
\begin{split}
F_Y(y) = P(Y \leq y) = P(X \in A_y) = \int_0^{e_y} f_X(x)dx = 1 -e^{-e^y}
\end{split}
$$
-  Ao derivarmos $1 -e^{-e^y}$ em função de $y$ obtemos $f_Y(y) = e^ye^{-e^y}$.


#### Exemplo
Caso fossemos resolver utilizando a derivada da inversa, temos que $r(x) = \log x \implies r^{-1}(x) = e^x$ e a derivada de $r^{-1}(y)$ é $e^y$. Logo,
$$
f_Y(y) = f_X(r^{-1}(y)) \left| \dfrac{dr^{-1}(y)}{dy}\right| = f_X(e^y)|e^y| = e^{-e^y}e^y
$$

### Exemplo

Mas de quê tudo isso importa para mim que só quero saber de *machine learning*?

#### Exemplo com *Distribution Shift*
Geralmente realizamos a otimização de um modelo utilizando amostras $\{x_1, y_1, \dots, x_n, y_n\}$ em que consideramos cada par $x_i, y_i$ é uma amostra das variáveis aleatórias $(X, Y) \sim D$ ($D$ é a distribuição conjunta). Em diversas aplicações, é comum que estejamos interessados em aplicar o nosso modelo em uma distribuição $\tilde D$ que é um pouco diferente, por exemplo:

-  $D$ são os dados coletados previamente em um processo seletivo, e a maioria dos aplicantes eram homens.
-  $\tilde D$ é a distribuição de candidatos no momento presente, onde há maior paridade de gênero.



Para simplificar o problema, vamos considerar que $X,Y$ são contínuas, e que estamos buscando por modelos lineares $h(x) = \theta x$. Nosso objetivo é resolver:
$$
\min_\theta \mathbb E_{\tilde D}[(h(X) - Y)^2]
$$
$$
\begin{split}
\mathbb E_{\tilde D}[(h(X) - Y)^2] = \int_\mathbb R \int_\mathbb R ( \theta x - y)^2 \tilde f_{X, Y}(x, y) dy dx 
\end{split}
$$


Utilizando o que foi visto hoje, podemos realizar a seguinte transformação:
$$
\tilde f_{X,Y}(x, y) = \tilde f_{Y\mid X}(y \mid x) \tilde f_X(x) 
$$
Vamos supor que $D$ e $\tilde D$ possuem a mesma relação entre $Y$ e $X$, isto é, $f_{Y\mid X} = \tilde f_{Y\mid X}$. Logo:
$$
\begin{split}
\int_\mathbb R \int_\mathbb R ( \theta x - y)^2 \tilde f_{X, Y}(x, y) dy dx  = \int_\mathbb R \int_\mathbb R ( \theta x - y)^2 \tilde f_{Y\mid X}(y \mid x) \tilde f_X(x) dy dx \\
=  \int_\mathbb R \int_\mathbb R ( \theta x - y)^2 f_{Y\mid X}(y \mid x) \tilde f_X(x) dy dx
\end{split}
$$


Vamos multiplicar e dividir por $f_X$:
$$
\begin{split}
\int_\mathbb R \int_\mathbb R ( \theta x - y)^2 f_{Y\mid X}(y \mid x) \tilde f_X(x) dy dx = \int_\mathbb R \int_\mathbb R ( \theta x - y)^2 f_{Y\mid X}(y \mid x) \dfrac{\tilde f_X(x)}{f_X(x)} f_X(x) dy dx
\end{split}
$$
Vamos chamar $\alpha(x) = \dfrac{\tilde f_X(x)}{f_X(x)}$. Então:
$$
\int_\mathbb R \int_\mathbb R ( \theta x - y)^2 f_{Y\mid X}(y \mid x) f_X(x) \alpha(x) dy dx = \mathbb E_D[(h( X) - Y)^2 \alpha(X)]
$$
Concluímos que $E_{\tilde D}[(h(X) - Y)^2] = \mathbb E_D[(h(X) - Y)^2 \alpha(X)]$. Podemos então resolver o nosso problema com um algoritmo de otimização em que cada amostra $(x_i, y_i)$ será ponderada pelo fator $\alpha(x_i)$. (Precisamos aindar entender como estimar a função $\alpha$).