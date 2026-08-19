# 📖 Chapter 5.1: Two Discrete Random Variables — Summary

*Textbook Chapter Link: [Chapter 5.1: Two Discrete Random Variables](https://www.probabilitycourse.com/chapter5/5_1_0_joint_distributions.php)*

이 장은 두 개 이상의 이산형 확률변수가 결합되어 분포를 이룰 때의 수학적 분석 기법(결합 PMF/CDF, 주변 분포, 조건부 분포, 독립성, 이변수 함수 및 조건부 기댓값/분산의 성질)을 요약 정리함.

---

## 5.1.1 Joint PMF
* **결합 확률질량함수 (Joint PMF, $P_{X,Y}(x,y)$)**:
    * 두 이산확률변수 $X$와 $Y$가 동시에 각각 특정 값 $x$와 $y$를 취할 확률을 정의하는 함수임.
        $$P_{X,Y}(x,y) = P(X = x, Y = y)$$
    * **성질**:
        1. $0 \le P_{X,Y}(x,y) \le 1$
        2. 모든 가능한 $x, y$에 대한 총합은 1임: $\sum_{x \in R_X} \sum_{y \in R_Y} P_{X,Y}(x,y) = 1$
* **주변 확률질량함수 (Marginal PMF)**:
    * 결합 PMF로부터 단일 확률변수 $X$ 또는 $Y$의 독자적인 PMF를 얻는 과정으로, 상대방 변수가 취할 수 있는 모든 확률을 더하여(소거하여) 구함.
        $$P_X(x) = \sum_{y \in R_Y} P_{X,Y}(x,y), \qquad P_Y(y) = \sum_{x \in R_X} P_{X,Y}(x,y)$$

---

## 5.1.2 Joint CDF
* **결합 누적분포함수 (Joint Cumulative Distribution Function, $F_{X,Y}(x,y)$)**:
    * 두 변수 $X, Y$가 각각 기준값 $x, y$ 이하일 확률을 매핑하는 함수로, 모든 실수 $x, y$에 대해 정의됨.
        $$F_{X,Y}(x,y) = P(X \le x, Y \le y)$$
* **주변 누적분포함수 (Marginal CDF)**:
    * 한 변수의 기준값을 무한대($\infty$)로 보냄으로써 상대 변수의 CDF를 얻음.
        $$F_X(x) = F_{X,Y}(x, \infty), \qquad F_Y(y) = F_{X,Y}(\infty, y)$$

---

## 5.1.3 Conditioning and Independence
사건 또는 특정 변수값이 주어졌을 때의 조건부 확률, 조건부 기댓값(상수 버전), 그리고 독립성을 다룸.

* **조건부 PMF & CDF (Conditional PMF & CDF)**:
    * 특정 사건 $A$가 주어졌을 때:
        $$P_{X|A}(x) = P(X=x \mid A) = \frac{P(X=x \text{ and } A)}{P(A)}$$
    * 타 확률변수의 관측값 $Y=y$가 주어졌을 때 ($P_Y(y) > 0$):
        $$P_{X|Y}(x|y) = P(X=x \mid Y=y) = \frac{P_{X,Y}(x,y)}{P_Y(y)}$$
        $$F_{X|Y}(x|y) = P(X \le x \mid Y=y) = \sum_{t \le x} P_{X|Y}(t|y)$$
* **조건부 기댓값 (Conditional Expectation — 상수 버전)**:
    * 특정 조건이 상수로 고정되었으므로, 계산 결과는 **상수(값)**로 얻어짐.
    * 사건 $A$ 하의 기댓값: $E[X \mid A] = \sum_{x_i \in R_X} x_i P_{X|A}(x_i)$
    * $Y=y$ 조건 하의 기댓값: $E[X \mid Y=y] = \sum_{x_i \in R_X} x_i P_{X|Y}(x_i \mid y)$
    * 조건부 LOTUS: $E[g(X) \mid A] = \sum_{x_i \in R_X} g(x_i) P_{X|A}(x_i)$
* **전체 기댓값의 법칙 (Law of Total Expectation — 합산 버전)**:
    * 표본 공간의 분할 $B_1, B_2, \dots$ 에 대해:
        $$E[X] = \sum_{i} E[X \mid B_i]P(B_i)$$
    * 이산형 확률변수 $Y$의 전체 영역에 대해:
        $$E[X] = \sum_{y_j \in R_Y} E[X \mid Y=y_j]P_Y(y_j)$$
* **이산형 변수의 독립성 (Independence)**:
    * 두 확률변수 $X$와 $Y$가 독립이라는 것은, 모든 $x, y$에 대해 다음이 성립함을 뜻함.
        $$P_{X,Y}(x,y) = P_X(x)P_Y(y) \quad \Longleftrightarrow \quad P_{X|Y}(x|y) = P_X(x)$$

---

## 5.1.4 Functions of Two Discrete Random Variables
* **PMF 유도**: 두 변수의 조합으로 정의되는 새로운 변수 $Z = g(X,Y)$의 PMF는 해당 $z$ 값을 만족하는 모든 순서쌍 $(x,y)$의 결합 확률을 합하여 구함.
    $$P_Z(z) = \sum_{(x,y): g(x,y)=z} P_{X,Y}(x,y)$$
* **이차원 LOTUS (2D LOTUS)**:
    $Z$의 PMF를 구하지 않고도 결합 PMF를 가중치로 가하여 $Z$의 기댓값을 직접 연산할 수 있음.
    $$E[g(X,Y)] = \sum_{x \in R_X} \sum_{y \in R_Y} g(x,y) P_{X,Y}(x,y)$$

---

## 5.1.5 Conditional Expectation
조건부 기댓값을 확률변수 관점에서 재정의하고, 반복 기댓값/분산의 일반 법칙을 다룸.

* **확률변수로서의 조건부 기댓값 ($E[X \mid Y]$)**:
    * 조건으로 특정 숫자 $y$가 아닌 확률변수 $Y$ 그 자체를 주면, $E[X \mid Y]$는 $Y$의 값에 따라 달라지는 **$Y$의 함수 $g(Y)$**가 됨.
    * 입력값인 확률변수 $Y$가 랜덤이므로, 출력값인 $E[X \mid Y]$ 역시 상수가 아니라 **그 자체로 확률변수**임.
* **아는 것 꺼내기 성질 (Taking out what is known)**:
    * 조건부 기댓값 기호 내에 이미 조건으로 걸려 있는 변수 $X$의 함수가 곱해져 있으면, 이는 상수 취급하여 기호 밖으로 꺼낼 수 있음.
        $$E[g(X)h(Y) \mid X] = g(X) E[h(Y) \mid X]$$
* **반복 기댓값의 법칙 / 전체 기댓값의 법칙 (Law of Iterated Expectations / Law of Total Expectation — 확률변수 버전)**:
    * 확률변수 $E[X \mid Y]$의 기댓값을 취하면 조건부 기호가 소거되며 원래 $X$의 평균과 동일해짐.
        $$E[E[X \mid Y]] = E[X]$$
* **조건부 분산 (Conditional Variance)**:
    * $Y$가 주어졌을 때 $X$의 변동성 지표로, 표기에 따라 확률변수 또는 상수가 됨.
    * **확률변수 버전**: $\text{Var}(X \mid Y) = E[X^2 \mid Y] - (E[X \mid Y])^2$
    * **상수 버전**: $\text{Var}(X \mid Y=y) = E[X^2 \mid Y=y] - (E[X \mid Y=y])^2$
* **전체 분산의 법칙 (Law of Total Variance)**:
    * 임의의 두 확률변수 $X$와 $Y$에 대해, $X$의 무조건부 분산은 '조건부 분산의 기댓값'과 '조건부 기댓값의 분산'의 합으로 쪼갤 수 있음.
        $$\text{Var}(X) = E[\text{Var}(X \mid Y)] + \text{Var}(E[X \mid Y])$$
    * **물리적 의미**: 조건화($Y$)를 거치면 정보가 추가되므로 $X$의 평균적인 불확실성은 감소함($E[\text{Var}(X \mid Y)] \le \text{Var}(X)$). 이때 줄어든 불확실성의 양은 조건부 기댓값 자체의 변동성($\text{Var}(E[X \mid Y])$)과 일치함.

---

## 5.1.6 Solved Problems

### **Example 5.1 (Marginal PMF와 독립성)**
**[Problem]**
Let $X$ and $Y$ be discrete random variables with joint PMF given by the table below:

| $P_{X,Y}(x,y)$ | $Y=1$ | $Y=2$ |
| :--- | :--- | :--- |
| **$X=0$** | $1/6$ | $1/3$ |
| **$X=1$** | $1/3$ | $1/6$ |

1. Find the marginal PMFs, $P_X(x)$ and $P_Y(y)$.
2. Are $X$ and $Y$ independent?

---

**[Solution]**
1. **Marginal PMFs 구하기**: (가로합 및 세로합 계산)
    * **$P_X(x)$**:
        * $P_X(0) = P_{X,Y}(0,1) + P_{X,Y}(0,2) = \frac{1}{6} + \frac{1}{3} = \frac{1}{2}$
        * $P_X(1) = P_{X,Y}(1,1) + P_{X,Y}(1,2) = \frac{1}{3} + \frac{1}{6} = \frac{1}{2}$
    * **$P_Y(y)$**:
        * $P_Y(1) = P_{X,Y}(0,1) + P_{X,Y}(1,1) = \frac{1}{6} + \frac{1}{3} = \frac{1}{2}$
        * $P_Y(2) = P_{X,Y}(0,2) + P_{X,Y}(1,2) = \frac{1}{3} + \frac{1}{6} = \frac{1}{2}$
2. **독립성 판정**:
    * $P_{X,Y}(0,1) = \frac{1}{6}$ 임.
    * $P_X(0) \cdot P_Y(1) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$ 임.
    * $P_{X,Y}(0,1) \ne P_X(0)P_Y(1)$ 이므로, 두 변수 $X$와 $Y$는 **서로 독립이 아님 (종속임).**
