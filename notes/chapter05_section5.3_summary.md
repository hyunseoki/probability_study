# 📖 Chapter 5.3: Covariance and Bivariate Normal — Summary

*Textbook Chapter Link: [Chapter 5.3: Covariance & Bivariate Normal](https://www.probabilitycourse.com/chapter5/5_3_1_covariance_correlation.php)*

이 장은 두 확률변수의 선형적 관계성을 측정하는 지표인 공분산(Covariance)과 상관계수(Correlation), 그리고 다변량 확률 통계의 핵심인 이변량 정규분포(Bivariate Normal Distribution)의 성질과 공식들을 요약 정리함.

---

## 1. 공분산과 상관계수 (Covariance & Correlation, 5.3.1)
* **공분산 (Covariance, $\text{Cov}(X,Y)$)**:
    * 두 확률변수의 공동 변화 양상(선형적 연관성)을 측정하는 지표임.
        $$\text{Cov}(X,Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]$$
    * **핵심 성질**:
        1. 자기 자신과의 공분산: $\text{Cov}(X,X) = \text{Var}(X)$
        2. 대칭성: $\text{Cov}(X,Y) = \text{Cov}(Y,X)$
        3. 선형성: $\text{Cov}(aX + b, cY + d) = ac\,\text{Cov}(X,Y)$
        4. **분산의 확장 공식 (합의 분산)**:
            $$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X,Y)$$
            $$\text{Var}\left( \sum_{i=1}^{n} a_i X_i \right) = \sum_{i=1}^{n} a_i^2 \text{Var}(X_i) + 2 \sum_{i < j} a_i a_j \text{Cov}(X_i, X_j)$$
        5. **독립성과 관계**: 두 변수가 독립이면 $E[XY]=E[X]E[Y]$가 성립하여 $\text{Cov}(X,Y)=0$ (무상관, Uncorrelated)이 됨. **단, 그 역은 일반적으로 성립하지 않음.** (선형 이외의 관계가 존재할 수 있기 때문임)
* **상관계수 (Correlation Coefficient, $\rho(X,Y)$)**:
    * 공분산을 각 표준편차의 곱으로 나누어, 척도(Scale)에 무관하도록 $[-1, 1]$ 범위로 표준화한 지표임.
        $$\rho(X,Y) = \rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$$
    * **성질**:
        1. 범위: $-1 \le \rho(X,Y) \le 1$
        2. 두 변수가 독립이면 $\rho(X,Y) = 0$ 임.
        3. $\rho(X,Y) = 1$ 또는 $-1$ 이면, 두 변수는 완벽한 선형 관계($Y = aX + b$)를 띰.

---

## 2. 이변량 정규분포 (Bivariate Normal Distribution, 5.3.2)
* **공동 정규변수의 정의 (Jointly Normal)**:
    * 두 확률변수 $X$와 $Y$의 임의의 선형 결합 $aX + bY$가 항상 일변량 정규분포를 따를 때, $X, Y$를 공동 정규변수라고 함.
* **결합 PDF 공식**:
    * 5개의 파라미터(각 변수의 평균 $\mu_X, \mu_Y$, 표준편차 $\sigma_X, \sigma_Y$, 상관계수 $\rho$)로 정의됨.
    $$f_{X,Y}(x,y) = \frac{1}{2\pi \sigma_X \sigma_Y \sqrt{1-\rho^2}} \exp \left\{ -\frac{1}{2(1-\rho^2)} \left[ \frac{(x-\mu_X)^2}{\sigma_X^2} - 2\rho \frac{(x-\mu_X)(y-\mu_Y)}{\sigma_X\sigma_Y} + \frac{(y-\mu_Y)^2}{\sigma_Y^2} \right] \right\}$$
* **핵심 성질**:
    1. **무상관과 독립의 동치성**: 일반적인 변수들과 달리, 공동 정규분포를 따르는 두 변수에 대해서는 **무상관($\rho = 0$)과 독립은 완전한 동치 조건임.**
        $$\rho(X,Y) = 0 \quad \Longleftrightarrow \quad X \text{와 } Y \text{는 서로 독립임}$$
    2. **주변 분포**: $X \sim N(\mu_X, \sigma_X^2)$ 이고 $Y \sim N(\mu_Y, \sigma_Y^2)$ 임.
    3. **조건부 분포**: $X=x$가 주어졌을 때 $Y$의 조건부 분포 역시 정규분포를 따름.
        $$Y \mid X=x \sim N\left( \mu_Y + \rho \frac{\sigma_Y}{\sigma_X}(x-\mu_X), \; \sigma_Y^2(1-\rho^2) \right)$$
        * **조건부 기댓값 (회귀식)**: $E[Y \mid X=x] = \mu_Y + \rho \frac{\sigma_Y}{\sigma_X}(x-\mu_X)$
        * **조건부 분산 (오차)**: $\text{Var}(Y \mid X=x) = \sigma_Y^2(1-\rho^2)$
          *(상관계수가 존재하면 정보가 추가되어 불확실성(분산)이 $1-\rho^2$ 비율만큼 감소함)*

---

## 3. Solved Problems (5.3 연습문제)

### **Example 5.3 (공분산 연산과 독립성)**
**[Problem]**
Let $X \sim N(0, 1)$ and $W$ be an independent random variable with $P(W = 0) = P(W = 1) = \frac{1}{2}$. 
Define $Y = X$ if $W=0$, and $Y = -X$ if $W=1$.
1. Show that $Y \sim N(0, 1)$.
2. Calculate $\text{Cov}(X,Y)$.
3. Are $X$ and $Y$ independent?

---

**[Solution]**
1. **$Y \sim N(0,1)$ 증명**:
    * $Y$의 CDF를 전체 확률의 법칙으로 전개함.
        $$F_Y(y) = P(Y \le y) = P(Y \le y \mid W=0)P(W=0) + P(Y \le y \mid W=1)P(W=1)$$
        $$= \frac{1}{2} P(X \le y \mid W=0) + \frac{1}{2} P(-X \le y \mid W=1)$$
    * $X$와 $W$는 독립이므로 조건부가 소거되며, 정규분포의 대칭성에 의해 $-X \sim N(0,1)$ 이므로 $P(-X \le y) = \Phi(y)$ 임.
        $$F_Y(y) = \frac{1}{2} \Phi(y) + \frac{1}{2} \Phi(y) = \Phi(y)$$
    * 따라서 $Y \sim N(0, 1)$ 임.
2. **$\text{Cov}(X,Y)$ 구하기**:
    * $E[X] = 0$ 이고 $E[Y] = 0$ 이므로, $\text{Cov}(X,Y) = E[XY]$ 임.
    * LOTUS와 전체 기댓값의 법칙을 적용함.
        $$E[XY] = E[XY \mid W=0]P(W=0) + E[XY \mid W=1]P(W=1)$$
        $$= \frac{1}{2} E[X^2] + \frac{1}{2} E[-X^2] = \frac{1}{2} E[X^2] - \frac{1}{2} E[X^2] = 0$$
    * **정답**: $\text{Cov}(X,Y) = 0$ (즉, 두 변수는 무상관임)
3. **독립성 판정**:
    * 두 변수의 합 $Z = X+Y$를 정의해봄.
        * $W=0 \implies Z = 2X$ (확률 1/2)
        * $W=1 \implies Z = 0$ (확률 1/2)
    * 따라서 $Z$는 $z=0$ 지점에서 점 질량(Point mass) $\frac{1}{2}$을 갖는 혼합 확률 변수이며, 그 PDF는 다음과 같음.
        $$f_Z(z) = \frac{1}{2} \delta(z) + \frac{1}{4\sqrt{2\pi}} e^{-\frac{z^2}{8}}$$
    * $X$와 $Y$는 모두 정규분포를 따르지만, 그 합인 $Z$는 정규분포가 아님.
    * 만약 $X$와 $Y$가 독립(공동정규분포)이었다면 독립인 정규변수의 합은 반드시 정규분포를 따라야 함.
    * 따라서 $X$와 $Y$는 **서로 독립이 아님 (종속임).**
    *(주의: 이 예제는 두 변수의 공분산이 0이지만 서로 독립이 아닌 대표적인 반례를 보여줌)*
