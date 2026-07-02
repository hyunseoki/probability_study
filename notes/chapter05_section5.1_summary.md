# 📖 Chapter 5.1: Two Discrete Random Variables — Summary

*Textbook Chapter Link: [Chapter 5.1: Two Discrete Random Variables](https://www.probabilitycourse.com/chapter5/5_1_0_joint_distributions.php)*

이 장은 두 개 이상의 이산형 확률변수가 결합되어 분포를 이룰 때의 수학적 분석 기법(결합 PMF/CDF, 주변 분포, 조건부 분포, 독립성, 이변수 함수 및 조건부 기댓값과 Law of Total Expectation)을 요약 정리함.

---

## 1. 결합 PMF와 주변 PMF (Joint PMF & Marginal PMF)
* **결합 확률질량함수 (Joint Probability Mass Function, $P_{X,Y}(x,y)$)**:
    * 두 이산확률변수 $X$와 $Y$가 동시에 각각 특정 값 $x$와 $y$를 취할 확률을 정의하는 함수임.
        $$P_{X,Y}(x,y) = P(X = x, Y = y)$$
    * **성질**:
        1. $0 \le P_{X,Y}(x,y) \le 1$
        2. 모든 가능한 $x, y$에 대한 총합은 1임: $\sum_{x \in R_X} \sum_{y \in R_Y} P_{X,Y}(x,y) = 1$
* **주변 확률질량함수 (Marginal PMF)**:
    * 결합 PMF로부터 단일 확률변수 $X$ 또는 $Y$의 독자적인 PMF를 얻는 과정으로, 상대방 변수가 취할 수 있는 모든 확률을 더하여(소거하여) 구함.
        $$P_X(x) = \sum_{y \in R_Y} P_{X,Y}(x,y), \qquad P_Y(y) = \sum_{x \in R_X} P_{X,Y}(x,y)$$

---

## 2. 결합 CDF (Joint CDF)
* **결합 누적분포함수 (Joint Cumulative Distribution Function, $F_{X,Y}(x,y)$)**:
    * 두 변수 $X, Y$가 각각 기준값 $x, y$ 이하일 확률을 매핑하는 함수로, 모든 실수 $x, y$에 대해 정의됨.
        $$F_{X,Y}(x,y) = P(X \le x, Y \le y)$$
* **주변 누적분포함수 (Marginal CDF)**:
    * 한 변수의 기준값을 무한대($\infty$)로 보냄으로써 상대 변수의 CDF를 얻음.
        $$F_X(x) = F_{X,Y}(x, \infty), \qquad F_Y(y) = F_{X,Y}(\infty, y)$$

---

## 3. 조건부 분포와 독립성 (Conditioning & Independence)
* **조건부 PMF (Conditional PMF, $P_{X|Y}(x|y)$)**:
    * $Y = y$라는 사건이 일어났다는 전제 하에, $X$가 $x$일 확률임. (정의역 상 $P_Y(y) > 0$ 조건 필요)
        $$P_{X|Y}(x|y) = P(X=x \mid Y=y) = \frac{P_{X,Y}(x,y)}{P_Y(y)}$$
* **이산형 변수의 독립성 (Independence)**:
    * 두 확률변수 $X$와 $Y$가 독립이라는 것은, 모든 $x, y$에 대해 다음이 성립함을 뜻함.
        $$P_{X,Y}(x,y) = P_X(x)P_Y(y) \quad \Longleftrightarrow \quad P_{X|Y}(x|y) = P_X(x)$$

---

## 4. 두 이산확률변수의 함수 (Functions of Two Discrete RVs)
* **PMF 유도**: 두 변수의 조합으로 정의되는 새로운 변수 $Z = g(X,Y)$의 PMF는 해당 $z$ 값을 만족하는 모든 순서쌍 $(x,y)$의 결합 확률을 합하여 구함.
    $$P_Z(z) = \sum_{(x,y): g(x,y)=z} P_{X,Y}(x,y)$$
* **이차원 LOTUS (2D LOTUS)**:
    $Z$의 PMF를 구하지 않고도 결합 PMF를 가중치로 가하여 $Z$의 기댓값을 직접 연산할 수 있음.
    $$E[g(X,Y)] = \sum_{x \in R_X} \sum_{y \in R_Y} g(x,y) P_{X,Y}(x,y)$$

---

## 5. 조건부 기댓값과 전체 기댓값의 법칙 (Conditional Expectation & Law of Total Expectation)
* **조건부 기댓값 (Conditional Expectation)**:
    * $Y=y$가 주어졌을 때 $X$의 기댓값으로, $y$의 값에 따라 결과가 정해지는 **$y$의 함수**임.
        $$E[X \mid Y=y] = \sum_{x \in R_X} x P_{X|Y}(x|y)$$
    * 만약 특정 관측값 $y$를 지정하지 않은 채 $E[X \mid Y]$로 쓰면, 이는 확률변수 $Y$에 의존하는 **새로운 확률변수**가 됨.
* **전체 기댓값의 법칙 (Law of Total Expectation / Law of Iterated Expectations)**:
    * 조건부 기댓값 $E[X \mid Y]$라는 확률변수의 기댓값을 취하면, 조건으로 걸려 있던 $Y$의 무작위성이 소거되어 원래 $X$의 평균과 동일해짐.
        $$E[E[X \mid Y]] = E[X]$$
    * *유도*:
        $$E[E[X \mid Y]] = \sum_{y} E[X \mid Y=y] P_Y(y) = \sum_{y} \sum_{x} x \frac{P_{X,Y}(x,y)}{P_Y(y)} P_Y(y) = \sum_{x} x \sum_{y} P_{X,Y}(x,y) = E[X]$$

---

## 6. Solved Problems (5.1 연습문제)

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
