# 📖 Chapter 4.2: Special Continuous Distributions — Summary

*Textbook Chapter Link: [Chapter 4.2: Special Continuous Distributions](https://www.probabilitycourse.com/chapter4/4_2_1_uniform.php)*

이 장은 대표적인 연속형 확률 분포(균등분포, 지수분포, 정규분포)의 성질과 더불어, 새로 추가된 감마분포(Gamma Distribution)의 수학적 성질(감마 함수 계산법 포함) 및 기타 부록 수록 분포들에 대해 요약 정리함.

---

## 1. 균등 분포 (Uniform Distribution)
* **정의**: 특정 구간 $[a, b]$ 내의 모든 지점에서 나타날 확률밀도가 균일(Constant)한 분포임.
* **표기**: $X \sim \text{Uniform}(a, b)$
* **PDF & CDF**:
    $$f_X(x) = \begin{cases} \frac{1}{b-a} & a \le x \le b \\ 0 & \text{otherwise} \end{cases}, \qquad F_X(x) = \begin{cases} 0 & x < a \\ \frac{x-a}{b-a} & a \le x \le b \\ 1 & x > b \end{cases}$$
* **기댓값과 분산**:
    $$E[X] = \frac{a+b}{2}, \qquad \text{Var}(X) = \frac{(b-a)^2}{12}$$

---

## 2. 지수 분포 (Exponential Distribution)
* **정의**: 특정 사건이 발생할 때까지 걸리는 대기 시간을 모델링하는 분포임.
* **파라미터**: 사건 발생율 $\lambda \quad (\lambda > 0)$
* **표기**: $X \sim \text{Exponential}(\lambda)$
* **PDF & CDF**:
    $$f_X(x) = \begin{cases} \lambda e^{-\lambda x} & x \ge 0 \\ 0 & \text{otherwise} \end{cases}, \qquad F_X(x) = \begin{cases} 1 - e^{-\lambda x} & x \ge 0 \\ 0 & \text{otherwise} \end{cases}$$
* **기댓값과 분산**:
    $$E[X] = \frac{1}{\lambda}, \qquad \text{Var}(X) = \frac{1}{\lambda^2}$$
* **무기억성 (Memoryless Property)**: 연속형 중 무기억성을 가지는 유일한 분포임.
    $$P(X > s+t \mid X > s) = P(X > t) \quad (\text{모든 } s, t \ge 0\text{에 대해})$$

---

## 3. 정규 분포 (Normal / Gaussian Distribution)
* **정의**: 평균 $\mu$를 중심으로 좌우 대칭인 종 모양(Bell-shaped)의 곡선을 띠는 가우시안 분포임.
* **표기**: $X \sim N(\mu, \sigma^2)$
* **확률밀도함수 (PDF)**:
    $$f_X(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \quad (-\infty < x < \infty)$$
* **기댓값과 분산**: $E[X] = \mu, \quad \text{Var}(X) = \sigma^2$
* **표준화 (Standardization)**:
    * 임의의 정규분포 $X$를 평균이 0이고 분산이 1인 표준정규분포 $Z \sim N(0, 1)$로 변환함.
        $$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$
    * 표준정규 CDF 기호 $\Phi(z) = P(Z \le z)$의 성질: $\Phi(-z) = 1 - \Phi(z)$
    * **구간 확률 계산**: $P(a \le X \le b) = \Phi\left(\frac{b-\mu}{\sigma}\right) - \Phi\left(\frac{a-\mu}{\sigma}\right)$

---

## 4. 감마 분포 (Gamma Distribution)
지수 분포 및 정규 분포와 매우 긴밀한 관계를 맺고 있는 중요한 연속형 분포임. 감마분포를 이해하기 위해서는 먼저 감마 함수를 정의해야 함.

### (1) 감마 함수 (Gamma Function, $\Gamma(\alpha)$)
팩토리얼(Factorial) 함수를 실수 및 복소수 영역으로 확장한 특수 함수임.
* **정의**: 
    $$\Gamma(\alpha) = \int_{0}^{\infty} x^{\alpha - 1} e^{-x} \, dx \quad (\alpha > 0 \text{ 일 때})$$
* **핵심 수학적 성질**:
    1. **점화식**: $\Gamma(\alpha + 1) = \alpha \Gamma(\alpha)$
    2. **팩토리얼과의 관계**: 자연수 $n$에 대해, $\Gamma(n) = (n-1)!$
    3. **경계값**: $\Gamma(1) = 1, \quad \Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$
    4. **중요 적분 공식 (유도 공식)**:
        $$\int_{0}^{\infty} x^{\alpha - 1} e^{-\lambda x} \, dx = \frac{\Gamma(\alpha)}{\lambda^{\alpha}} \quad (\alpha, \lambda > 0 \text{ 일 때})$$

### (2) 감마 분포 (Gamma Distribution)
* **정의**: 여러 개의 독립적인 지수분포 대기시간의 합 등을 다룰 때 주로 유도되는 연속형 분포임.
* **파라미터**: 모양 파라미터 $\alpha > 0$, 발생율 파라미터 $\lambda > 0$
* **표기**: $X \sim \text{Gamma}(\alpha, \lambda)$
* **확률밀도함수 (PDF)**:
    $$f_X(x) = \begin{cases} \frac{\lambda^{\alpha} x^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)} & x > 0 \\ 0 & \text{otherwise} \end{cases}$$
* **기댓값과 분산**:
    $$E[X] = \frac{\alpha}{\lambda}, \qquad \text{Var}(X) = \frac{\alpha}{\lambda^2}$$

---

## 5. 기타 분포 (Other Distributions, 4.2.5)
* Beta, Weibull, Cauchy 등 실무에서 쓰이는 기타 연속형 분포들은 교재 부록(Appendix)에 구체적인 수식과 성질이 나열되어 있음.
* 교재 저자는 이 수식들을 억지로 암기할 필요는 없으며, 확률변수의 일반 이론만 명확히 이해하고 있다면 부록을 참고하여 언제든 활용할 수 있다고 안내함.

---

## 6. Solved Problems (4.2 연습문제)

### **Example 4.7 (감마 함수 계산)**
**[Problem]**
1. Find $\Gamma\left(\frac{7}{2}\right)$.
2. Find the value of the following integral:
    $$I = \int_{0}^{\infty} x^{6} e^{-5x} \, dx$$

---

**[Solution]**
1. **$\Gamma\left(\frac{7}{2}\right)$ 구하기**: 점화식 $\Gamma(\alpha+1) = \alpha\Gamma(\alpha)$ 과 경계값 $\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}$ 를 이용함.
    $$\Gamma\left(\frac{7}{2}\right) = \frac{5}{2} \Gamma\left(\frac{5}{2}\right) = \frac{5}{2} \cdot \frac{3}{2} \Gamma\left(\frac{3}{2}\right) = \frac{5}{2} \cdot \frac{3}{2} \cdot \frac{1}{2} \Gamma\left(\frac{1}{2}\right) = \frac{15}{8}\sqrt{\pi}$$
2. **적분 계산**: 감마 적분 공식 $\int_{0}^{\infty} x^{\alpha - 1} e^{-\lambda x} \, dx = \frac{\Gamma(\alpha)}{\lambda^{\alpha}}$ 에 $\alpha = 7, \lambda = 5$ 를 대입함.
    $$I = \int_{0}^{\infty} x^{6} e^{-5x} \, dx = \frac{\Gamma(7)}{5^7} = \frac{6!}{5^7} = \frac{720}{78125} \approx 0.0092$$

---

### **Example 4.8 (정규분포 확률)**
**[Problem]**
Let $X \sim N(\mu=175, \sigma^2=6^2)$. Find the probability $P(172 \le X \le 187)$.
*(Use $\Phi(0.5) \approx 0.6915$, $\Phi(2) \approx 0.9772$)*

---

**[Solution]**
변수 표준화 $Z = \frac{X-175}{6} \sim N(0, 1)$ 를 취함.
* $x=172 \implies z = \frac{172-175}{6} = -0.5$
* $x=187 \implies z = \frac{187-175}{6} = 2$
따라서:
$$P(-0.5 \le Z \le 2) = \Phi(2) - \Phi(-0.5) = \Phi(2) - (1 - \Phi(0.5))$$
$$= 0.9772 - (1 - 0.6915) = 0.9772 - 0.3085 = 0.6687$$
* **정답**: 약 **$66.87\%$** 임.
