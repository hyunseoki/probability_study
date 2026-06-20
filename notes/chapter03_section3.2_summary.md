# 📖 Chapter 3.2: More about Discrete Random Variables — Summary

*Textbook Chapter Link: [Chapter 3.2: More about Discrete Random Variables](https://www.probabilitycourse.com/chapter3/3_2_1_cdf.php)*

이 장은 이산확률변수의 누적분포함수(CDF), 평균적인 위치를 나타내는 기댓값(Expectation), 그리고 데이터의 흩어짐 정도를 나타내는 분산(Variance)과 표준편차의 수학적 성질 및 확률변수의 함수 $g(X)$의 분포 연산법을 요약 정리함.

---

## 1. 누적분포함수 (Cumulative Distribution Function, CDF)
* **정의**: 확률변수 $X$가 특정 값 $x$ 이하일 확률을 나타내는 함수임. 이산형과 연속형을 불문하고 모든 확률변수에 대해 정의됨.
    $$F_X(x) = P(X \le x) \quad (\text{모든 } x \in \mathbb{R} \text{에 대해})$$
* **이산형 변수의 CDF 특징**:
    * 계단 모양(Step Function)의 형태를 띰.
    * 확률이 존재하는 원소 $x_i$ 지점에서 $P_X(x_i)$ 크기만큼 불연속적인 점프(Jump)가 발생함.
* **CDF의 3대 핵심 성질**:
    1. **비감소성 (Non-decreasing)**: $x_1 < x_2 \implies F_X(x_1) \le F_X(x_2)$
    2. **극한값**: 
        $$\lim_{x \to -\infty} F_X(x) = 0, \quad \lim_{x \to \infty} F_X(x) = 1$$
    3. **우연속성 (Right-continuous)**: 임의의 $x$에 대해 우극한값은 함숫값과 동일함.
        $$\lim_{t \to x^+} F_X(t) = F_X(x)$$
* **CDF를 활용한 구간 확률 계산**:
    $$P(a < X \le b) = F_X(b) - F_X(a)$$

---

## 2. 기댓값 (Expectation / Expected Value)
* **정의**: 확률변수 $X$가 취할 수 있는 값들을 확률로 가중 평균한 값으로, 확률분포의 무게중심(평균)에 해당함.
    $$E[X] = \sum_{x \in R_X} x P_X(x)$$
    *(단, 위 무한급수가 절대수렴할 때, 즉 $\sum |x| P_X(x) < \infty$ 일 때만 정의됨)*
* **기댓값의 성질 (선형성, Linearity)**:
    1. 임의의 상수 $a, b$에 대해: $E[aX + b] = aE[X] + b$
    2. **두 변수의 독립 여부와 상관없이 항상 성립**: $E[X + Y] = E[X] + E[Y]$
    3. 두 변수 $X, Y$가 **독립**이면 곱의 기댓값은 각각의 곱과 같음: $E[XY] = E[X]E[Y]$

---

## 3. 확률 변수의 함수 (Functions of Random Variables, $Y = g(X)$)
* **PMF 유도**: 새로운 확률변수 $Y = g(X)$의 PMF는 $g(X)=y$를 만족시키는 모든 $x$의 확률들을 더해서 구함.
    $$P_Y(y) = P(g(X) = y) = \sum_{x: g(x)=y} P_X(x)$$
* **무의식적 통계학자의 법칙 (Law of the Unconscious Statistician, LOTUS)**:
    * $Y = g(X)$의 기댓값을 구하기 위해 굳이 $Y$의 PMF인 $P_Y(y)$를 먼저 구하지 않고, 기존 변수 $X$의 PMF $P_X(x)$를 활용해 직접 기댓값을 계산할 수 있음.
    $$E[g(X)] = \sum_{x \in R_X} g(x) P_X(x)$$

---

## 4. 분산과 표준편차 (Variance & Standard Deviation)
* **분산 (Variance, $\text{Var}(X)$)**: 확률변수 $X$가 평균($E[X]$)으로부터 떨어져 있는 편차의 제곱의 평균임. 데이터가 평균 주위에 얼마나 조밀하게 모여 있는지 혹은 넓게 펴져 있는지를 나타냄.
    $$\text{Var}(X) = E[(X - E[X])^2]$$
* **실전 계산 공식 (Computational Formula)**:
    $$\text{Var}(X) = E[X^2] - (E[X])^2$$
* **표준편차 (Standard Deviation, $\text{SD}(X)$)**: 분산의 양의 제곱근으로, 확률변수와 동일한 물리적 단위를 가지게 함.
    $$\text{SD}(X) = \sigma_X = \sqrt{\text{Var}(X)}$$
* **분산의 성질**:
    1. 비음성: $\text{Var}(X) \ge 0$ (상수 집합이 아닌 한 항상 양수임)
    2. 선형 확장: $\text{Var}(aX + b) = a^2 \text{Var}(X)$ (상수 $b$는 흩어진 정도에 영향을 주지 않음)
    3. **독립인 두 변수** $X, Y$에 대해: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$
        *(일반적으로 독립이 아닌 경우 공분산(Covariance) 항이 추가됨)*

---

## 5. 5대 이산형 확률분포의 기댓값 및 분산 요약표

| 분포명 | 기호 ($X \sim$) | 기댓값 $E[X]$ | 분산 $\text{Var}(X)$ |
| :--- | :--- | :--- | :--- |
| **베르누이** | $\text{Bernoulli}(p)$ | $p$ | $p(1-p)$ |
| **이항분포** | $\text{Binomial}(n, p)$ | $np$ | $np(1-p)$ |
| **기하분포** | $\text{Geometric}(p)$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ |
| **파스칼** | $\text{Pascal}(r, p)$ | $\frac{r}{p}$ | $\frac{r(1-p)}{p^2}$ |
| **푸아송** | $\text{Poisson}(\lambda)$ | $\lambda$ | $\lambda$ |

---

## 6. Detailed Solutions for Chapter 3.2 Examples

### **Example 3.3 (LOTUS의 적용)**
**[Problem]**
Let $X$ be a discrete random variable with the following PMF:
$$P_X(x) = \begin{cases} 0.2 & x = -1 \\ 0.5 & x = 0 \\ 0.3 & x = 2 \\ 0 & \text{otherwise} \end{cases}$$
Let $Y = X^2$. 
1. Find the PMF of $Y$.
2. Calculate $E[Y]$ using the PMF of $Y$.
3. Calculate $E[Y]$ directly using LOTUS, and verify that both results are identical.

---

**[Solution]**

#### 1. PMF of $Y$ ($P_Y(y)$)
$X$가 가질 수 있는 값 $R_X = \{-1, 0, 2\}$에 대응하는 $Y = X^2$의 값 $R_Y$를 구함.
* $X = -1 \implies Y = (-1)^2 = 1$
* $X = 0 \implies Y = 0^2 = 0$
* $X = 2 \implies Y = 2^2 = 4$
따라서 $Y$가 가질 수 있는 치역은 $R_Y = \{0, 1, 4\}$ 임.

각 $Y$값에 대응하는 확률을 구함:
* $P_Y(0) = P(X^2 = 0) = P(X = 0) = 0.5$
* $P_Y(1) = P(X^2 = 1) = P(X = -1) = 0.2$
* $P_Y(4) = P(X^2 = 4) = P(X = 2) = 0.3$

따라서 $Y$의 PMF는 다음과 같음.
$$P_Y(y) = \begin{cases} 0.5 & y = 0 \\ 0.2 & y = 1 \\ 0.3 & y = 4 \\ 0 & \text{otherwise} \end{cases}$$

#### 2. Calculate $E[Y]$ using $P_Y(y)$
기댓값의 정의를 적용함.
$$E[Y] = \sum_{y \in R_Y} y P_Y(y) = 0(0.5) + 1(0.2) + 4(0.3) = 0 + 0.2 + 1.2 = 1.4$$

#### 3. Calculate $E[X^2]$ directly using LOTUS
LOTUS 공식($E[g(X)] = \sum g(x) P_X(x)$)을 적용함.
$$E[X^2] = \sum_{x \in R_X} x^2 P_X(x)$$
$$E[X^2] = (-1)^2 P_X(-1) + 0^2 P_X(0) + 2^2 P_X(2)$$
$$E[X^2] = 1(0.2) + 0(0.5) + 4(0.3) = 0.2 + 0 + 1.2 = 1.4$$

**결론**: 두 방식으로 계산한 기댓값은 $1.4$로 완전히 동일하며, LOTUS를 사용하는 것이 새로운 PMF를 구하는 중간 연산 단계를 단축시킬 수 있어 훨씬 효율적임.

---

### **Example 3.4 (분산과 성질)**
**[Problem]**
Let $X \sim \text{Binomial}(n, p)$. Using the fact that $X$ can be written as the sum of $n$ independent Bernoulli random variables $X = I_1 + I_2 + \dots + I_n$ where $I_j \sim \text{Bernoulli}(p)$, find the variance of $X$.

---

**[Solution]**

#### 1. 베르누이 변수 $I_j$의 분산 구하기
각 $I_j$는 $0$ 또는 $1$의 값만을 가지는 베르누이 분포를 따름.
* **기댓값 $E[I_j]$**: $1(p) + 0(1-p) = p$
* **제곱의 기댓값 $E[I_j^2]$**: $1^2(p) + 0^2(1-p) = p$
* **분산 $\text{Var}(I_j)$**:
    $$\text{Var}(I_j) = E[I_j^2] - (E[I_j])^2 = p - p^2 = p(1-p)$$

#### 2. 독립변수 합의 분산 성질 적용
문제 조건에 따라 각 시행은 독립이므로, $I_1, I_2, \dots, I_n$은 서로 독립인 확률변수들임.
독립인 확률변수 합의 분산은 각각의 분산의 합과 같음.
$$\text{Var}(X) = \text{Var}(I_1 + I_2 + \dots + I_n) = \text{Var}(I_1) + \text{Var}(I_2) + \dots + \text{Var}(I_n)$$
$$\text{Var}(X) = \sum_{j=1}^{n} p(1-p) = n p (1-p)$$

**정답**: 이항분포 $X \sim \text{Binomial}(n, p)$의 분산은 **$np(1-p)$**임.
