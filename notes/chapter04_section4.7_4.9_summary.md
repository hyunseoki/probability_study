# 📖 Chapter 4.7 ~ 4.9: Special Continuous Distributions — Summary

*Textbook Chapter Link: [Chapter 4.7: Uniform Distribution](https://www.probabilitycourse.com/chapter4/4_7_1_uniform_dist.php)*

이 장은 연속형 확률변수 중 가장 널리 사용되는 3대 핵심 분포인 균등분포(Uniform), 지수분포(Exponential), 그리고 통계학의 근간이 되는 정규분포(Normal / Gaussian)의 정의, 수학적 성질(기댓값, 분산, 무기억성, 표준화)을 요약 정리함.

---

## 1. 균등 분포 (Uniform Distribution)
* **정의**: 특정 구간 $[a, b]$ 내의 모든 지점에서 발생할 확률밀도가 균일(Constant)한 분포임.
* **표기**: $X \sim \text{Uniform}(a, b)$
* **확률밀도함수 (PDF)**:
    $$f_X(x) = \begin{cases} \frac{1}{b-a} & a \le x \le b \\ 0 & \text{otherwise} \end{cases}$$
* **누적분포함수 (CDF)**: (구간 내에서 $x$의 증가에 따라 선형적으로 증가함)
    $$F_X(x) = \begin{cases} 0 & x < a \\ \frac{x-a}{b-a} & a \le x \le b \\ 1 & x > b \end{cases}$$
* **기댓값과 분산**:
    * **기댓값**: 구간의 정중앙 지점임.
        $$E[X] = \frac{a+b}{2}$$
    * **분산**: (적분을 통해 유도됨)
        $$\text{Var}(X) = \frac{(b-a)^2}{12}$$

---

## 2. 지수 분포 (Exponential Distribution)
* **정의**: 특정 사건이 한 번 발생할 때까지 걸리는 대기 시간(예: 전구 수명, 콜센터에 다음 전화가 올 때까지의 시간)을 모델링하는 분포임.
* **파라미터**: 사건 발생율 $\lambda \quad (\lambda > 0)$
* **표기**: $X \sim \text{Exponential}(\lambda)$
* **확률밀도함수 (PDF)**:
    $$f_X(x) = \begin{cases} \lambda e^{-\lambda x} & x \ge 0 \\ 0 & \text{otherwise} \end{cases}$$
* **누적분포함수 (CDF)**:
    $$F_X(x) = \begin{cases} 1 - e^{-\lambda x} & x \ge 0 \\ 0 & \text{otherwise} \end{cases}$$
* **기댓값과 분산**:
    * **기댓값**: $E[X] = \frac{1}{\lambda}$ (발생율이 $\lambda$일 때 평균 대기 시간은 그 역수임)
    * **분산**: $\text{Var}(X) = \frac{1}{\lambda^2}$

* **무기억성 (Memoryless Property)**:
    * 이미 $s$만큼 기다렸더라도, 추가로 $t$만큼 더 기다려야 할 확률은 처음부터 새로 $t$만큼 기다릴 확률과 완전히 동일함.
    * **수식**:
        $$P(X > s+t \mid X > s) = P(X > t) \quad (\text{모든 } s, t \ge 0 \text{에 대해})$$
    * **의의**: 연속형 확률변수 중 **무기억성을 가지는 유일한 분포**임. (이산형에서는 기하 분포가 유일함)

---

## 3. 정규 분포 (Normal / Gaussian Distribution)
* **정의**: 평균 $\mu$를 중심으로 좌우 대칭인 종 모양(Bell-shaped)의 곡선을 띠는 분포로, 자연계 및 사회학적 데이터 집계 시 가장 보편적으로 관측되는 분포임.
* **표기**: $X \sim N(\mu, \sigma^2)$ (여기서 $\mu$는 평균, $\sigma^2$은 분산)
* **확률밀도함수 (PDF)**:
    $$f_X(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \quad (-\infty < x < \infty)$$
* **기댓값과 분산**:
    * $E[X] = \mu$
    * $\text{Var}(X) = \sigma^2$

* **표준 정규 분포 (Standard Normal Distribution, $Z$)**:
    * 평균이 $0$이고 분산이 $1$인 정규분포이며, 보통 변수 $Z$로 표기함.
    * **표기**: $Z \sim N(0, 1)$
    * **CDF 기호**: 표준정규분포의 CDF는 고유한 기호인 대문자 파이 **$\Phi(z)$**로 정의함.
        $$\Phi(z) = P(Z \le z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{z} e^{-\frac{t^2}{2}} \, dt$$
    * **대칭 성질**: 평균 0을 기준으로 대칭이므로 다음이 성립함.
        $$\Phi(-z) = 1 - \Phi(z)$$

* **정규분포의 표준화 (Standardization)**:
    * 임의의 정규분포 $X \sim N(\mu, \sigma^2)$는 변환을 통해 항상 표준정규분포 $Z$로 바꿀 수 있음. (이 과정을 통해 복잡한 정규분포 적분을 표준정규분포 표 $\Phi(z)$ 하나로 전부 해결함)
    * **표준화 변환 공식**:
        $$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$
    * **확률 계산**:
        $$P(a \le X \le b) = P\left( \frac{a - \mu}{\sigma} \le Z \le \frac{b - \mu}{\sigma} \right) = \Phi\left(\frac{b-\mu}{\sigma}\right) - \Phi\left(\frac{a-\mu}{\sigma}\right)$$

---

## 4. 3대 연속형 확률분포 요약표

| 분포명 | 기호 ($X \sim$) | PDF $f_X(x)$ | 기댓값 $E[X]$ | 분산 $\text{Var}(X)$ |
| :--- | :--- | :--- | :--- | :--- |
| **균등분포** | $\text{Uniform}(a, b)$ | $\frac{1}{b-a} \quad (a \le x \le b)$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| **지수분포** | $\text{Exponential}(\lambda)$ | $\lambda e^{-\lambda x} \quad (x \ge 0)$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |
| **정규분포** | $N(\mu, \sigma^2)$ | $\frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |

---

## 5. Detailed Solutions for Chapter 4.7 ~ 4.9 Examples

### **Example 4.5 (지수 분포의 무기억성 증명)**
**[Problem]**
Let $X \sim \text{Exponential}(\lambda)$. Prove the memoryless property:
$$P(X > s+t \mid X > s) = P(X > t) \quad \text{for } s, t \ge 0$$

---

**[Solution]**

#### 1. CDF를 통한 초과 확률 $P(X > x)$ 정의
지수분포의 CDF는 $F_X(x) = 1 - e^{-\lambda x} \quad (x \ge 0)$ 임.
따라서 사건 $X > x$의 확률은 여사건으로 다음과 같음.
$$P(X > x) = 1 - F_X(x) = e^{-\lambda x}$$

#### 2. 조건부 확률 공식 적용
조건부 확률 정의 $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ 에 대입함.
사건 $A = \{X > s+t\}$ 이고 $B = \{X > s\}$ 일 때, $t \ge 0$ 이므로 두 사건의 교집합은 결국 $A$가 됨 ($X > s+t \implies X > s$).
$$P(X > s+t \mid X > s) = \frac{P(X > s+t \text{ 이고 } X > s)}{P(X > s)} = \frac{P(X > s+t)}{P(X > s)}$$

#### 3. 수식 계산 및 비교
앞서 정의한 초과 확률 공식을 대입하여 나눗셈을 수행함.
$$\frac{P(X > s+t)}{P(X > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = \frac{e^{-\lambda s} \cdot e^{-\lambda t}}{e^{-\lambda s}} = e^{-\lambda t}$$
이 결과식 $e^{-\lambda t}$는 정확히 처음부터 기다린 확률인 $P(X > t)$와 같음.
$$P(X > s+t \mid X > s) = P(X > t)$$
* **결론**: 지수분포의 무기억성이 수학적으로 증명되었음.

---

### **Example 4.6 (정규분포의 표준화와 확률 계산)**
**[Problem]**
The height of adult men in a certain population is normally distributed with mean $\mu = 175\text{ cm}$ and standard deviation $\sigma = 6\text{ cm}$. Find the probability that a randomly selected man is:
1. Shorter than $169\text{ cm}$.
2. Between $172\text{ cm}$ and $187\text{ cm}$.
*(Use $\Phi(1) \approx 0.8413$, $\Phi(0.5) \approx 0.6915$, $\Phi(2) \approx 0.9772$)*

---

**[Solution]**

남성의 키를 확률변수 $X$라 하면, $X \sim N(\mu=175, \sigma^2=6^2)$ 임.

#### 1. $169\text{ cm}$ 미만일 확률 ($P(X < 169)$)
표준화 공식 $Z = \frac{X - \mu}{\sigma}$ 를 적용함.
$$P(X < 169) = P\left( \frac{X - 175}{6} < \frac{169 - 175}{6} \right) = P(Z < -1)$$
* **대칭성 적용**:
    $$P(Z < -1) = \Phi(-1) = 1 - \Phi(1)$$
* **값 대입**:
    $$1 - 0.8413 = 0.1587$$
* **정답**: 약 **$15.87\%$** 임.

#### 2. $172\text{ cm}$ 와 $187\text{ cm}$ 사이일 확률 ($P(172 \le X \le 187)$)
양 끝점을 각각 표준화함.
* $x = 172 \implies z = \frac{172 - 175}{6} = -0.5$
* $x = 187 \implies z = \frac{187 - 175}{6} = 2$
따라서 구하고자 하는 확률은 다음과 같음.
$$P(-0.5 \le Z \le 2) = \Phi(2) - \Phi(-0.5)$$
* **대칭성 풀기**:
    $$\Phi(-0.5) = 1 - \Phi(0.5)$$
    $$P(-0.5 \le Z \le 2) = \Phi(2) - [1 - \Phi(0.5)] = \Phi(2) + \Phi(0.5) - 1$$
* **값 대입**:
    $$0.9772 + 0.6915 - 1 = 1.6687 - 1 = 0.6687$$
* **정답**: 약 **$66.87\%$** 임.
