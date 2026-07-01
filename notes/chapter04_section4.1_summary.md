# 📖 Chapter 4.1: Continuous Random Variables and Their Distributions — Summary

*Textbook Chapter Link: [Chapter 4.1: Continuous Random Variables](https://www.probabilitycourse.com/chapter4/4_1_0_continuous_random_vars_distributions.php)*

이 장은 연속확률변수의 핵심적인 기초 이론(PDF, CDF, 기댓값, 분산)과 확률변수의 함수 변환 기법($Y = g(X)$)을 통합 요약 정리함.

---

## 1. 연속확률변수와 PDF (Continuous RVs & PDF)
* **연속확률변수의 정의**: 치역(Range, $R_X$)이 실수 집합 $\mathbb{R}$ 또는 특정 실수 구간과 같이 셀 수 없는 비가산 집합(Uncountable Set)인 확률변수이며, 누적분포함수(CDF)가 모든 실수에서 연속함수인 분포임.
* **지점 확률 0의 성질**: 임의의 단일 지점 $x$에서 값을 취할 확률은 항상 $0$임.
    $$P(X = x) = 0 \quad (\text{모든 } x \in \mathbb{R}\text{에 대해})$$
    ➔ 이로 인해 구간의 끝점 포함 여부는 확률에 영향을 주지 않음 ($P(a \le X \le b) = P(a < X < b)$).
* **확률밀도함수 (Probability Density Function, PDF, $f_X(x)$)**:
    * 정의: 구간 $[a, b]$에 속할 확률을 적분식으로 매핑하는 함수임.
        $$P(a \le X \le b) = \int_{a}^{b} f_X(x) \, dx$$
    * **PDF가 만족해야 할 공리**:
        1. 비음성: $f_X(x) \ge 0 \quad (\text{모든 } x \in \mathbb{R})$
        2. 총 면적 1: $\int_{-\infty}^{\infty} f_X(x) \, dx = 1$
    * **CDF와의 관계**:
        $$F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt \quad \Longleftrightarrow \quad f_X(x) = \frac{d}{dx} F_X(x)$$

---

## 2. 기댓값과 분산 (Expected Value & Variance)
* **기댓값 (Expected Value, $E[X]$)**:
    $$E[X] = \int_{-\infty}^{\infty} x f_X(x) \, dx \quad \left(\text{단, } \int_{-\infty}^{\infty} |x| f_X(x) \, dx < \infty \text{ 일 때}\right)$$
* **무의식적 통계학자의 법칙 (LOTUS)**: $Y = g(X)$의 기댓값을 $Y$의 PDF 없이 기존 $X$의 PDF로 계산함.
    $$E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) \, dx$$
* **선형성 (Linearity)**: 변수들의 독립 여부와 상관없이 항상 다음이 성립함.
    * $E[aX + b] = aE[X] + b$
    * $E[X + Y] = E[X] + E[Y]$
* **분산 (Variance, $\text{Var}(X)$)**:
    $$\text{Var}(X) = E[X^2] - (E[X])^2 \quad \left(\text{여기서 } E[X^2] = \int_{-\infty}^{\infty} x^2 f_X(x) \, dx\right)$$
    * 성질: $\text{Var}(aX + b) = a^2 \text{Var}(X)$

---

## 3. 확률변수의 함수 변환 (Functions of Continuous RVs)
연속확률변수 $X$에 대해 새로운 변수 $Y = g(X)$의 PDF $f_Y(y)$를 유도하는 두 가지 기법임.

### (1) 누적분포함수법 (CDF Method)
$Y$의 CDF 정의식에서 출발하여 $X$의 부등식으로 변형한 뒤, 최종 미분하여 PDF를 구하는 기법임.
1. $F_Y(y) = P(Y \le y) = P(g(X) \le y)$ 식을 세움.
2. 부등식을 $X$의 범위로 변환하여 $F_X(\cdot)$식으로 나타냄.
3. 양변을 $y$에 대해 미분함: $f_Y(y) = \frac{d}{dy} F_Y(y)$.

### (2) 일대일 매핑 변환 공식 (One-to-One Mapping Formula)
함수 $y = g(x)$가 엄격한 단조함수(strictly monotonic)여서 일대일 대응이고 미분 가능할 때 다음 공식을 적용함.
$$f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right| = \frac{f_X(x)}{|g'(x)|} \quad (\text{단, } x = g^{-1}(y))$$
* 여기서 $\left| \frac{dx}{dy} \right|$ 항은 1차원 야코비안(Jacobian)으로 넓이를 보존하는 스케일링 비율 역할을 함.

---

## 4. Solved Problems (4.1 연습문제)

### **Example 4.1**
**[Problem]**
Let $X$ be a continuous random variable with PDF:
$$f_X(x) = \begin{cases} c x^2 & 0 < x < 2 \\ 0 & \text{otherwise} \end{cases}$$
Find the constant $c$, the CDF $F_X(x)$, and the expected value $E[X]$.

---

**[Solution]**
1. **$c$ 구하기**: PDF 총면적이 1이어야 하므로,
    $$\int_{0}^{2} c x^2 \, dx = 1 \implies \left[ \frac{c}{3} x^3 \right]_{0}^{2} = 1 \implies \frac{8c}{3} = 1 \implies c = \frac{3}{8}$$
2. **CDF $F_X(x)$ 구하기**: $F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt$ 에 대입함.
    * $x < 0 \implies F_X(x) = 0$
    * $0 \le x < 2 \implies F_X(x) = \int_{0}^{x} \frac{3}{8} t^2 \, dt = \frac{x^3}{8}$
    * $x \ge 2 \implies F_X(x) = 1$
3. **기댓값 $E[X]$ 구하기**:
    $$E[X] = \int_{0}^{2} x \cdot \left(\frac{3}{8} x^2\right) \, dx = \int_{0}^{2} \frac{3}{8} x^3 \, dx = \left[ \frac{3}{32} x^4 \right]_{0}^{2} = 1.5$$

---

### **Example 4.2**
**[Problem]**
Let $X$ be a continuous random variable with PDF $f_X(x)$. Let $Y = X^2$. Find the PDF of $Y$ for $y > 0$.

---

**[Solution]**
일대일 대응이 아니므로 CDF Method를 적용함.
1. **CDF 식 세우기 ($y > 0$)**:
    $$F_Y(y) = P(Y \le y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y}) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$$
2. **양변을 $y$에 대해 미분하여 PDF 구하기**: (Chain Rule 적용)
    $$f_Y(y) = \frac{d}{dy} \left[ F_X(\sqrt{y}) - F_X(-\sqrt{y}) \right] = f_X(\sqrt{y}) \frac{1}{2\sqrt{y}} - f_X(-\sqrt{y}) \left(-\frac{1}{2\sqrt{y}}\right)$$
    $$f_Y(y) = \frac{1}{2\sqrt{y}} \left[ f_X(\sqrt{y}) + f_X(-\sqrt{y}) \right] \quad (y > 0 \text{ 일 때})$$
