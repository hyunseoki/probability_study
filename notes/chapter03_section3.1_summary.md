# 📖 Chapter 3.1: Discrete Random Variables — Basic Concepts Summary

*Textbook Chapter Link: [Chapter 3.1: Basic Concepts](https://www.probabilitycourse.com/chapter3/3_1_1_random_variables.php)*

이 장은 확률 변수(Random Variable)의 수학적 본질을 다루고, 특히 이산형 값을 가지는 이산확률변수(Discrete Random Variable)의 기초 개념(확률질량함수, 독립성) 및 실생활에서 널리 활용되는 5가지 대표적인 이산형 확률 분포들을 요약 정리함.

---

## 1. 확률 변수 (Random Variables)
* **정의**: 표본 공간 $\Omega$의 각 표본 원소(Outcome, $\omega$)를 실수 $\mathbb{R}$에 대응시키는 함수(Mapping)임.
    $$X: \Omega \rightarrow \mathbb{R}$$
* **의의**: 동전의 앞/뒷면, 주사위 눈금과 같은 정성적(Qualitative)인 실험 결과를 실수 형태로 나타냄으로써 더하기, 빼기, 평균 등의 수학적 대수 연산을 가능케 함.
* **표기법**: 확률 변수 자체는 대문자 $X, Y, Z$로 표기하며, 그 확률 변수가 가질 수 있는 구체적인 실수 표본값은 소문자 $x, y, z$로 표기함.
* **치역 (Range, $R_X$)**: 확률 변수 $X$가 가질 수 있는 모든 실수 값들의 집합임.
    $$R_X = \{x \in \mathbb{R} \mid X(\omega) = x \text{ for some } \omega \in \Omega\}$$

---

## 2. 이산확률변수와 확률질량함수 (Discrete RVs & PMF)
* **이산확률변수 (Discrete Random Variable)**: 치역 $R_X$가 유한집합(Finite)이거나 가산 무한집합(Countably Infinite)인 확률 변수임. 즉, 가질 수 있는 값들을 하나씩 셀 수 있는 경우를 말함.
* **확률질량함수 (Probability Mass Function, PMF, $P_X(x)$)**:
    * 이산확률변수 $X$가 특정한 값 $x$를 가질 확률을 매핑하는 함수임.
    * 정의: $P_X(x) = P(X = x) = P(\{\omega \in \Omega \mid X(\omega) = x\})$
* **PMF의 필수 조건 (Axioms for PMF)**:
    1. $0 \le P_X(x) \le 1 \quad (\text{모든 } x \in \mathbb{R} \text{에 대해})$
    2. $\sum_{x \in R_X} P_X(x) = 1$
    3. 임의의 사건 $A \subset R_X$에 대해, $P(X \in A) = \sum_{x \in A} P_X(x)$ 임.

---

## 3. 이산형 확률변수의 독립성 (Independence of Discrete RVs)
* **정의**: 두 이산확률변수 $X$와 $Y$가 독립이라는 것은 이들이 결합하여 가질 수 있는 임의의 값 $x, y$에 대해 다음 사건들이 서로 독립임을 의미함.
    $$P(X = x, Y = y) = P(X = x) P(Y = y)$$
* **결합 PMF 표현**: 독립인 두 변수 $X, Y$의 결합 확률질량함수(Joint PMF)는 각 변수의 개별 PMF(Marginal PMF)의 곱으로 분리됨.
    $$P_{X, Y}(x, y) = P_X(x) P_Y(y) \quad (\text{모든 } x, y \text{에 대해})$$

---

## 4. 5대 이산 확률 분포 (Special Discrete Distributions)

### (1) 베르누이 분포 (Bernoulli Distribution)
* **정의**: 결과가 오직 두 가지(성공 $1$, 실패 $0$)뿐인 시행(베르누이 시행)을 단 한 번 수행했을 때의 분포임.
* **파라미터**: 성공 확률 $p \quad (0 \le p \le 1)$
* **표기**: $X \sim \text{Bernoulli}(p)$
* **PMF**:
    $$P_X(x) = \begin{cases} p & x = 1 \\ 1-p & x = 0 \\ 0 & \text{otherwise} \end{cases}$$

### (2) 이항 분포 (Binomial Distribution)
* **정의**: 성공 확률이 $p$인 독립적인 베르누이 시행을 $n$번 반복했을 때 발생하는 총 성공 횟수 $X$의 분포임.
* **파라미터**: 시행 횟수 $n \in \{1, 2, \dots\}$, 성공 확률 $p$
* **표기**: $X \sim \text{Binomial}(n, p)$
* **PMF**: (성공할 $k$번을 고르는 조합 조합 수 $\binom{n}{k}$와 결합)
    $$P_X(k) = \binom{n}{k} p^k (1-p)^{n-k} \quad (k \in \{0, 1, \dots, n\})$$

### (3) 기하 분포 (Geometric Distribution)
* **정의**: 성공 확률이 $p$인 독립적인 베르누이 시행에서 **첫 번째 성공**이 일어날 때까지 수행해야 하는 총 시행 횟수 $X$의 분포임.
* **파라미터**: 성공 확률 $p$
* **표기**: $X \sim \text{Geometric}(p)$
* **PMF**: ($k-1$번의 실패 후 $k$번째에 성공함)
    $$P_X(k) = (1-p)^{k-1} p \quad (k \in \{1, 2, 3, \dots\})$$
* **무기억성 (Memoryless Property)**:
    * 이미 $m$번을 실패했더라도, 앞으로 추가로 $n$번 더 시행하여 성공할 확률은 처음부터 새로 $n$번 시행하여 성공할 확률과 완전히 동일함.
    $$P(X > m + n \mid X > m) = P(X > n) \quad (\text{단, } m, n \in \{1, 2, \dots\})$$

### (4) 파스칼 분포 (Pascal Distribution / Negative Binomial)
* **정의**: 성공 확률이 $p$인 독립적인 베르누이 시행에서 **$r$번째 성공**이 일어날 때까지 수행해야 하는 총 시행 횟수 $X$의 분포임.
* **파라미터**: 목표 성공 횟수 $r \in \{1, 2, \dots\}$, 성공 확률 $p$
* **표기**: $X \sim \text{Pascal}(r, p)$
* **PMF**: ($k-1$번째 시행까지 $r-1$번 성공하고, 마지막 $k$번째에 $r$번째 성공을 거두는 조건)
    $$P_X(k) = \binom{k-1}{r-1} p^r (1-p)^{k-r} \quad (k \in \{r, r+1, r+2, \dots\})$$
    *(참고: $r=1$인 파스칼 분포는 기하 분포와 완전히 일치함)*

### (5) 푸아송 분포 (Poisson Distribution)
* **정의**: 일정한 단위 시간 또는 공간 내에서 평균적으로 $\lambda$번 발생하는 사건이 실제로 $k$번 발생할 확률의 분포임. (예: 1시간 동안 콜센터에 걸려오는 전화의 수)
* **파라미터**: 평균 발생 횟수 $\lambda \quad (\lambda > 0)$
* **표기**: $X \sim \text{Poisson}(\lambda)$
* **PMF**:
    $$P_X(k) = \frac{e^{-\lambda} \lambda^k}{k!} \quad (k \in \{0, 1, 2, \dots\})$$
* **이항분포의 극한다항식 유도 (Poisson Approximation to Binomial)**:
    * 시행 횟수 $n$이 매우 크고($n \to \infty$) 성공 확률 $p$가 매우 작을 때($p \to 0$), 평균값 $\lambda = np$를 일정하게 유지하면 이항분포는 푸아송 분포로 수렴함.
    $$\lim_{\substack{n \to \infty \\ p \to 0, np=\lambda}} \binom{n}{k} p^k (1-p)^{n-k} = \frac{e^{-\lambda} \lambda^k}{k!}$$

---

## 5. Detailed Solutions for Chapter 3.1 Examples

### **Example 3.1 (이항 분포)**
**[Problem]**
A reliable communication channel transmits bits (0s or 1s). Due to noise, each bit has a probability $p = 0.01$ of being corrupted during transmission. Assume bit errors occur independently. If a message of $100$ bits is sent, find the probability that:
1. Exactly $2$ bits are corrupted.
2. At most $2$ bits are corrupted.

---

**[Solution]**

훼손된 비트의 수를 확률 변수 $X$라 정의함. 
각 비트의 에러 여부는 서로 독립인 베르누이 시행이므로, $X$는 이항 분포를 따름.
$$X \sim \text{Binomial}(n=100, p=0.01)$$

#### 1. Exactly $2$ bits corrupted ($P(X = 2)$)
이항분포 PMF 공식에 대입함.
$$P(X = 2) = \binom{100}{2} (0.01)^2 (0.99)^{98}$$
* **계산**:
    $$\binom{100}{2} = \frac{100 \times 99}{2} = 4950$$
    $$(0.01)^2 = 0.0001$$
    $$(0.99)^{98} \approx 0.3729$$
    $$P(X = 2) \approx 4950 \times 0.0001 \times 0.3729 \approx 0.1849$$
* **정답**: 정확히 2개의 비트가 훼손될 확률은 약 **$18.49\%$**임.

#### 2. At most $2$ bits corrupted ($P(X \le 2)$)
$X$가 가질 수 있는 값은 이산형이므로 $P(X \le 2) = P(X=0) + P(X=1) + P(X=2)$ 임.
* **$P(X=0)$**: $\binom{100}{0} (0.01)^0 (0.99)^{100} = (0.99)^{100} \approx 0.3660$
* **$P(X=1)$**: $\binom{100}{1} (0.01)^1 (0.99)^{99} = 100 \times 0.01 \times (0.99)^{99} = (0.99)^{99} \approx 0.3697$
* **$P(X=2)$**: $\approx 0.1849$
* **종합**:
    $$P(X \le 2) \approx 0.3660 + 0.3697 + 0.1849 = 0.9206$$
* **정답**: 최대 2개의 비트가 훼손될 확률은 약 **$92.06\%$**임.

---

### **Example 3.2 (푸아송 근사)**
**[Problem]**
Solve the first part of Example 3.1 (exactly $2$ corrupted bits out of $100$ with $p=0.01$) using the Poisson approximation, and compare the result.

---

**[Solution]**

이항분포를 푸아송 분포로 근사하기 위해 평균값 $\lambda$를 구함.
$$\lambda = n \times p = 100 \times 0.01 = 1$$
따라서 훼손 비트 수 $X$는 매개변수 $\lambda=1$인 푸아송 분포로 근사할 수 있음.
$$X \approx Y \sim \text{Poisson}(\lambda=1)$$

* **푸아송 PMF 대입 ($k=2$)**:
    $$P(Y = 2) = \frac{e^{-1} \cdot 1^2}{2!} = \frac{e^{-1}}{2} \approx \frac{0.367879}{2} \approx 0.1839$$
* **비교**:
    * 이항분포를 통한 정확한 계산 결과: $0.1849$
    * 푸아송 분포를 이용한 근사 계산 결과: $0.1839$
    * 두 결과의 절대 오차는 $0.0010$ (즉, 약 $0.1\%$ 차이)으로, $n$이 충분히 크고 $p$가 매우 작아 푸아송 근사가 매우 훌륭하게 작동함을 알 수 있음.
