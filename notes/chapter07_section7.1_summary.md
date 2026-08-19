# 📖 Chapter 7.1: Limit Theorems — Summary

*Textbook Chapter Link: [Chapter 7.1: Limit Theorems](https://www.probabilitycourse.com/chapter7/7_1_0_limit_theorems.php)*

이 장은 확률론과 통계학의 핵심 기둥인 **대수의 법칙(Law of Large Numbers, LLN)**과 **중심극한정리(Central Limit Theorem, CLT)**를 다룸. 다수의 독립 항의 합 및 표본 평균이 갖는 점근적(Asymptotic) 분포와 수렴 특성을 수학적으로 정리함.

---

## 1. 표본 평균의 기본 성질 (Sample Mean Properties)

서로 독립이고 동일한 분포를 따르는(i.i.d.) 확률변수열 $X_1, X_2, \dots, X_n$이 주어졌을 때:
* 평균: $E[X_i] = \mu < \infty$
* 분산: $\mathrm{Var}(X_i) = \sigma^2 < \infty$

### 표본 평균 (Sample Mean)
$$\overline{X} = \frac{X_1 + X_2 + \dots + X_n}{n} = \frac{1}{n}\sum_{i=1}^n X_i$$

* **기댓값**: 
  $$E[\overline{X}] = E\left[\frac{1}{n}\sum_{i=1}^n X_i\right] = \frac{1}{n} \sum_{i=1}^n E[X_i] = \frac{1}{n}(n\mu) = \mu$$
* **분산**:
  $$\mathrm{Var}(\overline{X}) = \mathrm{Var}\left(\frac{1}{n}\sum_{i=1}^n X_i\right) = \frac{1}{n^2}\sum_{i=1}^n \mathrm{Var}(X_i) = \frac{1}{n^2}(n\sigma^2) = \frac{\sigma^2}{n}$$
* **표준편차**:
  $$\sigma_{\overline{X}} = \frac{\sigma}{\sqrt{n}}$$

> **핵심 직관**: 표본의 크기 $n$이 커질수록 표본 평균 $\overline{X}$의 중심(기댓값)은 모평균 $\mu$를 유지하지만, 분산은 $\frac{1}{n}$에 비례하여 0으로 급격히 수축함. 즉, $\overline{X}$는 $\mu$ 근처로 집중됨.

---

## 2. 약한 대수의 법칙 (Weak Law of Large Numbers, WLLN)

### (1) 정리 내용
$X_1, X_2, \dots, X_n$이 평균이 $\mu < \infty$인 i.i.d. 확률변수열일 때, 임의의 양수 $\epsilon > 0$에 대하여 표본 평균 $\overline{X}$가 모평균 $\mu$와 $\epsilon$ 이상 차이 날 확률은 $n \to \infty$일 때 0으로 수렴함:

$$\lim_{n \to \infty} P(|\overline{X} - \mu| \ge \epsilon) = 0$$
$$\Longleftrightarrow \lim_{n \to \infty} P(|\overline{X} - \mu| < \epsilon) = 1$$

이는 표본 평균 $\overline{X}_n$이 모평균 $\mu$로 **확률 수렴(Convergence in Probability, $\overline{X}_n \xrightarrow{P} \mu$)**함을 의미함.

### (2) 증명 (유한 분산 $\sigma^2 < \infty$ 가정 시)
체비쇼프 부등식(Chebyshev's Inequality) $P(|Y - E[Y]| \ge \epsilon) \le \frac{\mathrm{Var}(Y)}{\epsilon^2}$에 $Y = \overline{X}$를 대입함:

$$P(|\overline{X} - \mu| \ge \epsilon) \le \frac{\mathrm{Var}(\overline{X})}{\epsilon^2} = \frac{\sigma^2}{n\epsilon^2}$$

여기서 $n \to \infty$ 극한을 취하면 우변이 0으로 수렴하므로:
$$\lim_{n \to \infty} P(|\overline{X} - \mu| \ge \epsilon) = 0$$

### (3) 통계적 의미 (빈도주의 확률의 정당화)
어떤 사건 $A$의 발생 여부를 지시 확률변수(Indicator) $X_i = 1_A$ ($P(X_i = 1) = P(A)$)로 두면, 표본 평균 $\overline{X} = \frac{n_A}{n}$는 $A$의 상대 도수(Relative Frequency)가 됨.
WLLN에 의해 시행 횟수 $n$이 커질수록 상대 도수는 이론적 확률 $P(A)$로 수렴함이 수학적으로 보장됨.

---

## 3. 중심극한정리 (Central Limit Theorem, CLT)

### (1) 정리 내용
$X_1, X_2, \dots, X_n$이 평균 $E[X_i] = \mu$, 분산 $\mathrm{Var}(X_i) = \sigma^2$ ($0 < \sigma^2 < \infty$)을 갖는 i.i.d. 확률변수열일 때, **정규화된 확률변수(Standardized RV)** $Z_n$의 누적분포함수(CDF)는 $n \to \infty$에 따라 표준정규분포 $N(0, 1)$의 CDF인 $\Phi(z)$로 수렴함.

$$Z_n = \frac{\overline{X} - \mu}{\sigma / \sqrt{n}} = \frac{\sum_{i=1}^n X_i - n\mu}{\sqrt{n}\sigma}$$

$$\lim_{n \to \infty} P(Z_n \le z) = \Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-t^2/2} \, dt$$

### (2) CLT의 핵심 특징과 의의
1. **분포 무관성**: $X_i$의 원래 분포가 이산형이든, 연속형이든, 혼합형이든, 비대칭이든 상관없이 **평균과 유한한 분산만 존재하면 합이나 평균은 정규분포에 가까워짐**.
2. **분포 수렴 (Convergence in Distribution)**: CLT는 PDF나 PMF의 점별 수렴이 아니라 누적확률인 **CDF의 수렴**을 나타냄 ($Z_n \xrightarrow{d} N(0, 1)$).
3. **표본 크기 기준 (Rule of Thumb)**: 일반적으로 $n \ge 30$이면 정규 근사가 매우 잘 들어맞음 (원 분포가 대칭에 가까울수록 더 작은 $n$으로도 우수한 근사를 보임).
4. **자연/공학계 응용**: 측정 오차, 통신 시스템의 가우스 잡음(Thermal Noise), 금융 자산의 누적 변동 등 다수의 독립적 미소 요인이 합산되는 물리 현상이 왜 정규분포를 따르는지 설명함.

### (3) CLT 문제 풀이 표준 3단계
1. **합산 변수 정의**: 관심 대상 변수를 $n$개의 i.i.d. 변수의 합으로 표현함: $Y = X_1 + X_2 + \dots + X_n$
2. **합의 평균과 분산 계산**:
   $$E[Y] = n\mu, \qquad \mathrm{Var}(Y) = n\sigma^2, \qquad \sigma_Y = \sqrt{n}\sigma$$
3. **표준화 및 표준정규분포표($\Phi$)를 통한 확률 근사**:
   $$P(y_1 \le Y \le y_2) = P\left(\frac{y_1 - n\mu}{\sqrt{n}\sigma} \le \frac{Y - n\mu}{\sqrt{n}\sigma} \le \frac{y_2 - n\mu}{\sqrt{n}\sigma}\right) \approx \Phi\left(\frac{y_2 - n\mu}{\sqrt{n}\sigma}\right) - \Phi\left(\frac{y_1 - n\mu}{\sqrt{n}\sigma}\right)$$

---

## 4. 이산확률변수의 연속성 수정 (Continuity Correction)

### (1) 필요성
$Y = \sum_{i=1}^n X_i$가 정수값만을 갖는 이산확률변수(예: 이항분포 $Binomial(n, p)$)일 때, 이를 연속형인 정규분포로 근사하면 경계 지점에서 오차가 발생함.

### (2) 수정 규칙 (단위 폭 1의 절반인 $\pm 0.5$를 보정)
정수 $l, u$에 대해:
* **구간 확률**:
  $$P(l \le Y \le u) = P\left(l - \frac{1}{2} \le Y \le u + \frac{1}{2}\right)$$
* **특정 단일점 확률**:
  $$P(Y = k) = P\left(k - \frac{1}{2} \le Y \le k + \frac{1}{2}\right)$$
* **부등호 형태별 보정 요약**:
  * $P(Y \ge l) \Longrightarrow P(Y \ge l - 0.5)$
  * $P(Y \le u) \Longrightarrow P(Y \le u + 0.5)$
  * $P(Y > l) = P(Y \ge l + 1) \Longrightarrow P(Y \ge l + 0.5)$
  * $P(Y < u) = P(Y \le u - 1) \Longrightarrow P(Y \le u - 0.5)$

---

## 5. 7.1 Solved Problems (대표 예제 및 적중 증명)

### **Example 7.1 (비행기 승객 무게 합산)**
**[Problem]**
비행기에 탑승하는 100명의 승객의 몸무게 $X_1, X_2, \dots, X_{100}$이 i.i.d.이고 평균 $\mu = 170\text{ lbs}$, 표준편차 $\sigma = 30\text{ lbs}$를 따른다고 하자. 전체 승객 무게 $W = \sum_{i=1}^{100} X_i$가 $18,000\text{ lbs}$를 초과할 확률 $P(W > 18000)$을 구하라.

**[Solution]**
1. 총합 $W$의 평균과 분산:
   * $E[W] = n\mu = 100 \times 170 = 17,000$
   * $\mathrm{Var}(W) = n\sigma^2 = 100 \times 30^2 = 90,000 \implies \sigma_W = \sqrt{90,000} = 300$
2. CLT 적용:
   $$P(W > 18000) = P\left(\frac{W - 17000}{300} > \frac{18000 - 17000}{300}\right) = P\left(Z > \frac{10}{3}\right)$$
   $$P(Z > 3.33) = 1 - \Phi(3.33) \approx 4.3 \times 10^{-4} = 0.00043$$

---

### **Example 7.2 (이산 랜덤워크와 연속성 수정)**
**[Problem]**
$X_1, \dots, X_{25}$가 i.i.d.이고 PMF가 $P(X_i = 1) = 0.6$, $P(X_i = -1) = 0.4$로 주어진다. $Y = \sum_{i=1}^{25} X_i$일 때, CLT와 연속성 수정을 이용하여 $P(4 \le Y \le 6)$을 구하라.

**[Solution]**
1. 개별 $X_i$의 평균과 분산:
   * $E[X_i] = (1)(0.6) + (-1)(0.4) = 0.2 = \frac{1}{5}$
   * $E[X_i^2] = (1)^2(0.6) + (-1)^2(0.4) = 1$
   * $\mathrm{Var}(X_i) = 1 - (0.2)^2 = 0.96 = \frac{24}{25}$
2. $Y$의 평균과 표준편차:
   * $E[Y] = 25 \times 0.2 = 5$
   * $\mathrm{Var}(Y) = 25 \times \frac{24}{25} = 24 \implies \sigma_Y = \sqrt{24} = 2\sqrt{6} \approx 4.899$
3. 연속성 수정 및 CLT 적용:
   $$P(4 \le Y \le 6) = P(3.5 \le Y \le 6.5)$$
   $$= P\left(\frac{3.5 - 5}{2\sqrt{6}} \le \frac{Y - 5}{2\sqrt{6}} \le \frac{6.5 - 5}{2\sqrt{6}}\right) = P(-0.3062 \le Z \le 0.3062)$$
   $$\approx \Phi(0.3062) - \Phi(-0.3062) = 2\Phi(0.3062) - 1 \approx 2(0.62025) - 1 = 0.2405$$

---

### **Example 7.3 (파티 샌드위치 부족 방지 문제)**
**[Problem]**
64명의 손님을 파티에 초대함. 각 손님이 필요로 하는 샌드위치 개수 $X_i$는 서로 독립이며 $0, 1, 2$개를 각각 확률 $\frac{1}{4}, \frac{1}{2}, \frac{1}{4}$로 소비함. 샌드위치가 부족하지 않을 확률이 $95\%$ 이상이 되도록 하려면 최소 몇 개의 샌드위치 $y$를 준비해야 하는가?

**[Solution]**
1. 개별 소비량 $X_i$의 평균과 분산:
   * $E[X_i] = 0\left(\frac{1}{4}\right) + 1\left(\frac{1}{2}\right) + 2\left(\frac{1}{4}\right) = 1$
   * $E[X_i^2] = 0^2\left(\frac{1}{4}\right) + 1^2\left(\frac{1}{2}\right) + 2^2\left(\frac{1}{4}\right) = \frac{3}{2}$
   * $\mathrm{Var}(X_i) = \frac{3}{2} - 1^2 = \frac{1}{2}$
2. 총 소비량 $Y = \sum_{i=1}^{64} X_i$:
   * $E[Y] = 64 \times 1 = 64$
   * $\mathrm{Var}(Y) = 64 \times \frac{1}{2} = 32 \implies \sigma_Y = \sqrt{32} = 4\sqrt{2} \approx 5.6569$
3. $P(Y \le y) \ge 0.95$ 조건 만족하는 $y$ 산출:
   $$P\left(\frac{Y - 64}{4\sqrt{2}} \le \frac{y - 64}{4\sqrt{2}}\right) \approx \Phi\left(\frac{y - 64}{4\sqrt{2}}\right) \ge 0.95$$
   $$\frac{y - 64}{4\sqrt{2}} \ge \Phi^{-1}(0.95) \approx 1.6449$$
   $$y \ge 64 + 1.6449(4\sqrt{2}) \approx 64 + 9.305 = 73.305$$
따라서 샌드위치를 **최소 74개** 준비해야 함.

---

### **Example 7.4 (지수분포 표본 평균의 신뢰 구간과 표본 크기 $n$)**
**[Problem]**
$X_1, \dots, X_n \sim \text{Exponential}(\lambda=1)$ i.i.d. 확률변수열이 있을 때, 표본 평균 $\overline{X}$가 $0.9 \le \overline{X} \le 1.1$ 범위에 들어올 확률이 $95\%$ 이상이 되도록 하는 최소 정수 $n$을 구하라.

**[Solution]**
1. 개별 변수 모수:
   * $E[X_i] = \frac{1}{\lambda} = 1, \quad \mathrm{Var}(X_i) = \frac{1}{\lambda^2} = 1$
2. 합 $Y = \sum_{i=1}^n X_i$ 및 $\overline{X} = \frac{Y}{n}$:
   * $E[Y] = n, \quad \mathrm{Var}(Y) = n \implies \sigma_Y = \sqrt{n}$
3. 확률 식 표준화:
   $$P(0.9 \le \overline{X} \le 1.1) = P(0.9n \le Y \le 1.1n) = P\left(\frac{0.9n - n}{\sqrt{n}} \le \frac{Y - n}{\sqrt{n}} \le \frac{1.1n - n}{\sqrt{n}}\right)$$
   $$= P\left(-0.1\sqrt{n} \le Z \le 0.1\sqrt{n}\right) \approx 2\Phi(0.1\sqrt{n}) - 1 \ge 0.95$$
4. $n$의 최솟값 계산:
   $$\Phi(0.1\sqrt{n}) \ge \frac{1 + 0.95}{2} = 0.975$$
   $$0.1\sqrt{n} \ge \Phi^{-1}(0.975) = 1.96 \implies \sqrt{n} \ge 19.6 \implies n \ge 19.6^2 = 384.16$$
$n$은 정수이므로 **$n \ge 385$**이어야 함.

---

### **Example 7.5 (MGF를 이용한 약한 대수의 법칙 증명)**
**[Problem]**
$X_1, \dots, X_n$이 평균 $E[X_i] = \mu$를 갖고 원점 주변 $[-c, c]$에서 유한한 적률생성함수(MGF) $M_X(s)$를 갖는 i.i.d. 확률변수열일 때, $\lim_{n \to \infty} M_{\overline{X}}(s) = e^{s\mu}$임을 증명하고 이를 통해 $\overline{X}$가 $\mu$로 수렴함을 보여라.

**[Proof]**
1. $\overline{X} = \frac{X_1 + \dots + X_n}{n}$의 MGF 전개:
   $$M_{\overline{X}}(s) = E\left[e^{s\frac{X_1+\dots+X_n}{n}}\right] = E\left[\prod_{i=1}^n e^{\frac{s}{n}X_i}\right] = \prod_{i=1}^n E\left[e^{\frac{s}{n}X_i}\right] = \left[M_X\left(\frac{s}{n}\right)\right]^n$$
2. $M_X(t)$의 $t=0$ 근방 테일러 급수(Taylor series):
   $$M_X(t) = M_X(0) + M_X'(0)t + o(t) = 1 + \mu t + o(t)$$
3. $t = \frac{s}{n}$ 대입 후 극한:
   $$\lim_{n \to \infty} M_{\overline{X}}(s) = \lim_{n \to \infty} \left[1 + \frac{s\mu}{n} + o\left(\frac{1}{n}\right)\right]^n = e^{s\mu}$$
$e^{s\mu}$는 상수 확률변수 $Y = \mu$ ($P(Y = \mu) = 1$)의 MGF와 정확히 일치하므로, 표본 평균 $\overline{X}$의 분포는 상수 $\mu$로 수렴함. $\blacksquare$

---

### **Example 7.6 (MGF를 이용한 중심극한정리 증명)**
**[Problem]**
$X_1, \dots, X_n$이 평균 $E[X_i] = \mu$, 분산 $\mathrm{Var}(X_i) = \sigma^2$을 갖고 유한한 MGF를 갖는 i.i.d. 변수열일 때, $Z_n = \frac{\overline{X} - \mu}{\sigma/\sqrt{n}}$의 MGF가 $e^{s^2/2}$로 수렴함을 보여 중심극한정리를 증명하라.

**[Proof]**
1. 표준화된 개별 확률변수 $Y_i = \frac{X_i - \mu}{\sigma}$ 정의:
   * $E[Y_i] = 0$, $\mathrm{Var}(Y_i) = E[Y_i^2] = 1$
2. $Z_n$ 표현:
   $$Z_n = \frac{\sum_{i=1}^n (X_i - \mu)}{\sqrt{n}\sigma} = \frac{1}{\sqrt{n}}\sum_{i=1}^n Y_i$$
3. $Z_n$의 MGF 전개:
   $$M_{Z_n}(s) = E\left[e^{\frac{s}{\sqrt{n}}\sum Y_i}\right] = \left[M_Y\left(\frac{s}{\sqrt{n}}\right)\right]^n$$
4. $M_Y(t)$의 2차 테일러 전개 ($E[Y]=0, E[Y^2]=1$ 활용):
   $$M_Y(t) = 1 + E[Y]t + \frac{E[Y^2]}{2!}t^2 + o(t^2) = 1 + 0 + \frac{t^2}{2} + o(t^2) = 1 + \frac{t^2}{2} + o(t^2)$$
5. $t = \frac{s}{\sqrt{n}}$ 대입 후 극한:
   $$\lim_{n \to \infty} M_{Z_n}(s) = \lim_{n \to \infty} \left[1 + \frac{s^2/2}{n} + o\left(\frac{1}{n}\right)\right]^n = e^{s^2/2}$$
$e^{s^2/2}$는 표준정규분포 $N(0, 1)$의 MGF이므로, MGF 연속성 정리(Levy's Continuity Theorem)에 의해 $Z_n$의 CDF는 표준정규분포의 CDF $\Phi(z)$로 수렴함 ($Z_n \xrightarrow{d} N(0,1)$). $\blacksquare$
