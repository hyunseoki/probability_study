# 📖 Chapter 4.1 ~ 4.4: Continuous Random Variables — Basic Concepts Summary

*Textbook Chapter Link: [Chapter 4: Continuous Random Variables](https://www.probabilitycourse.com/chapter4/4_1_1_continuous_rv.php)*

이 장은 치역이 비가산 집합(Uncountable Set)인 연속확률변수(Continuous Random Variable)의 수학적 기초를 다룸. 이산형과 달리 개별 지점에서의 확률이 $0$이 되는 독특한 성질을 이해하고, 이를 표현하기 위한 확률밀도함수(PDF)의 개념과 적분을 활용한 기댓값, 분산의 계산법을 요약 정리함.

---

## 1. 연속확률변수 (Continuous Random Variables)
* **정의**: 확률변수 $X$가 가질 수 있는 값의 범위(치역 $R_X$)가 실수 전체 집합 $\mathbb{R}$ 또는 실수 상의 특정 구간(Interval)과 같이 셀 수 없는 비가산 집합인 확률변수임.
* **이산형과의 결정적 차이 ($P(X=x) = 0$)**:
    * 이산형 확률변수는 개별 지점에서 0보다 큰 확률값을 가질 수 있으나, 연속확률변수는 **임의의 단일 지점 $x$에서 취할 확률이 항상 $0$**임.
        $$P(X = x) = 0 \quad (\text{모든 } x \in \mathbb{R} \text{에 대해})$$
    * 비유하자면, 수직선 상의 무한한 모래알 중 정확히 특정 모래알 하나를 집어낼 확률은 수학적으로 $0$인 것과 같음.
    * 따라서 연속확률변수에서는 개별 지점의 확률이 아니라, **"특정 구간에 속할 확률"**만을 유의미하게 계산함.
    * 이 성질 때문에 구간의 끝점 포함 여부가 확률에 영향을 주지 않음.
        $$P(a \le X \le b) = P(a < X \le b) = P(a \le X < b) = P(a < X < b)$$

---

## 2. 확률밀도함수 (Probability Density Function, PDF)
* **정의**: 연속확률변수 $X$가 특정 구간 $[a, b]$에 속할 확률을 적분식으로 나타내기 위해 정의된 함수 $f_X(x)$임.
    $$P(a \le X \le b) = \int_{a}^{b} f_X(x) \, dx$$

* **PDF의 필수 조건 (Axioms for PDF)**:
    1. **비음성 (Non-negativity)**: 모든 실수 $x$에 대해 $f_X(x) \ge 0$ 임.
    2. **총 면적은 1 (Total Area is 1)**: 실수 전체 공간에서의 적분값은 $1$임.
        $$\int_{-\infty}^{\infty} f_X(x) \, dx = 1$$

* **⚠️ 주의할 점 (PDF값과 확률의 차이)**:
    * **$f_X(x)$의 함숫값 자체는 확률이 아님.**
    * 확률은 면적(적분값)이므로, 개별 지점에서의 세로 높이인 $f_X(x)$의 값은 **$1$보다 커질 수 있음.** (예: 매우 좁은 구간에 확률이 집중되어 있다면 높이는 $100$이나 $\infty$에 가깝게 솟구칠 수 있음)
    * $f_X(x) \, dx$는 아주 미소한 구간 $[x, x+dx]$에 존재할 미소 확률을 나타냄.

* **누적분포함수(CDF)와의 수학적 관계**:
    * CDF $F_X(x)$는 PDF를 $-\infty$부터 $x$까지 누적 적분한 것임.
        $$F_X(x) = P(X \le x) = \int_{-\infty}^{x} f_X(t) \, dt$$
    * 미적분학의 기본 정리(Fundamental Theorem of Calculus)에 의해, CDF를 미분하면 PDF를 얻음.
        $$f_X(x) = \frac{d}{dx} F_X(x) \quad (\text{단, } F_X(x) \text{가 미분 가능한 지점에서})$$

---

## 3. 연속형 확률변수의 기댓값 (Expected Values)
* **정의**: 이산형의 합 공식($\sum$)이 연속형에서는 적분 공식($\int$)으로 확장됨.
    $$E[X] = \int_{-\infty}^{\infty} x f_X(x) \, dx$$
    *(단, 위 광의 적분이 절대수렴할 때, 즉 $\int_{-\infty}^{\infty} |x| f_X(x) \, dx < \infty$ 일 때만 정의됨)*

* **무의식적 통계학자의 법칙 (LOTUS)**:
    * 새로운 확률변수 $Y = g(X)$의 기댓값을 구할 때, $Y$의 PDF를 구하지 않고 기존 $X$의 PDF를 활용해 직접 계산할 수 있음.
        $$E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) \, dx$$

* **선형성 (Linearity)**:
    * 연속형 확률변수에서도 기댓값의 선형성 성질은 **독립 여부와 상관없이 항상 성립**함.
    * $E[aX + b] = aE[X] + b$
    * $E[X + Y] = E[X] + E[Y]$

---

## 4. 연속형 확률변수의 분산 (Variance)
* **정의**: 평균으로부터 떨어진 편차 제곱의 기댓값임.
    $$\text{Var}(X) = E[(X - E[X])^2] = \int_{-\infty}^{\infty} (x - E[X])^2 f_X(x) \, dx$$
* **실전 계산 공식**:
    $$\text{Var}(X) = E[X^2] - (E[X])^2$$
    *(여기서 $E[X^2] = \int_{-\infty}^{\infty} x^2 f_X(x) \, dx$ 임)*
* **성질**:
    * $\text{Var}(aX + b) = a^2 \text{Var}(X)$
    * 두 확률변수 $X, Y$가 **서로 독립**이면, $E[XY] = E[X]E[Y]$ 가 성립하므로 다음이 유도됨.
        $$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$$

---

## 5. Detailed Solutions for Chapter 4.1 ~ 4.4 Examples

### **Example 4.1 (PDF 성질과 CDF 유도)**
**[Problem]**
Let $X$ be a continuous random variable with PDF given by:
$$f_X(x) = \begin{cases} c x^2 & 0 < x < 2 \\ 0 & \text{otherwise} \end{cases}$$
1. Find the constant $c$.
2. Find the cumulative distribution function (CDF), $F_X(x)$.
3. Find $P(1 \le X \le 2)$.

---

**[Solution]**

#### 1. Constant $c$ 구하기
PDF의 총 면적 조건인 $\int_{-\infty}^{\infty} f_X(x) \, dx = 1$ 을 이용함.
$$\int_{0}^{2} c x^2 \, dx = 1$$
* **적분 계산**:
    $$\left[ \frac{c}{3} x^3 \right]_{0}^{2} = 1 \implies \frac{8c}{3} - 0 = 1 \implies c = \frac{3}{8}$$
* **정답**: $c = \frac{3}{8}$ 임.

#### 2. CDF $F_X(x)$ 구하기
정의 $F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt$ 를 적용하여 구간별로 누적 확률을 구함.
* **$x \le 0$ 일 때**: 누적된 면적이 전혀 없으므로 $F_X(x) = 0$ 임.
* **$0 < x < 2$ 일 때**:
    $$F_X(x) = \int_{0}^{x} \frac{3}{8} t^2 \, dt = \left[ \frac{1}{8} t^3 \right]_{0}^{x} = \frac{x^3}{8}$$
* **$x \ge 2$ 일 때**: 전체 면적이 다 누적되었으므로 $F_X(x) = 1$ 임.
* **정답**:
    $$F_X(x) = \begin{cases} 0 & x \le 0 \\ \frac{x^3}{8} & 0 < x < 2 \\ 1 & x \ge 2 \end{cases}$$

#### 3. $P(1 \le X \le 2)$ 구하기
CDF 또는 PDF의 구간 적분을 활용함. CDF가 더 계산이 간단하므로 $F_X(b) - F_X(a)$ 공식을 씀.
$$P(1 \le X \le 2) = F_X(2) - F_X(1) = 1 - \frac{1^3}{8} = 1 - \frac{1}{8} = \frac{7}{8}$$
* **정답**: $P(1 \le X \le 2) = \frac{7}{8}$ 임.

---

### **Example 4.2 (연속형 기댓값과 분산)**
**[Problem]**
For the random variable $X$ in Example 4.1, find the expected value $E[X]$ and the variance $\text{Var}(X)$.

---

**[Solution]**

$c = \frac{3}{8}$ 이므로 PDF는 $f_X(x) = \frac{3}{8}x^2 \quad (0 < x < 2)$ 임.

#### 1. 기댓값 $E[X]$ 계산
$$E[X] = \int_{0}^{2} x \cdot \left(\frac{3}{8}x^2\right) \, dx = \int_{0}^{2} \frac{3}{8} x^3 \, dx$$
* **적분 계산**:
    $$E[X] = \left[ \frac{3}{32} x^4 \right]_{0}^{2} = \frac{3}{32} \cdot 16 = \frac{3}{2} = 1.5$$
* **정답**: 기댓값 $E[X] = 1.5$ 임.

#### 2. 분산 $\text{Var}(X)$ 계산
$\text{Var}(X) = E[X^2] - (E[X])^2$ 공식을 쓰기 위해 먼저 $E[X^2]$을 구함.
$$E[X^2] = \int_{0}^{2} x^2 \cdot \left(\frac{3}{8}x^2\right) \, dx = \int_{0}^{2} \frac{3}{8} x^4 \, dx$$
* **적분 계산**:
    $$E[X^2] = \left[ \frac{3}{40} x^5 \right]_{0}^{2} = \frac{3}{40} \cdot 32 = \frac{96}{40} = \frac{12}{5} = 2.4$$
* **분산 공식 대입**:
    $$\text{Var}(X) = E[X^2] - (E[X])^2 = 2.4 - (1.5)^2 = 2.4 - 2.25 = 0.15$$
* **정답**: 분산 $\text{Var}(X) = 0.15$ 임.
