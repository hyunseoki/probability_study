# 📖 Chapter 4.10 ~ 4.12: Mixed Random Variables & Delta Function — Summary

*Textbook Chapter Link: [Chapter 4.10: Mixed Random Variables](https://www.probabilitycourse.com/chapter4/4_10_1_mixed_rvs.php)*

이 장은 이산형과 연속형의 특징이 결합된 혼합 확률 변수(Mixed Random Variable)의 수학적 분석법을 다룸. 불연속 점프가 존재하여 일반적인 미분이 불가능한 혼합형 CDF를 다루기 위해 물리학 및 신호처리에서 쓰이는 디랙 델타 함수(Dirac Delta Function)를 도입하고, 이를 통해 일반화된 PDF를 정의하여 기댓값을 효율적으로 연산하는 기법을 요약 정리함.

---

## 1. 혼합 확률 변수 (Mixed Random Variables)
* **정의**: 일부 구간에서는 연속적인 확률밀도를 가지면서, 특정 개별 지점(Point)에서는 0보다 큰 이산적인 확률(점 질량, Point Mass)을 동시에 갖는 복합적인 확률변수임.
* **실생활 예시**:
    * **주차 시간**: 주차장에 들어와 바로 회차하여 나간 차량들의 시간은 정확히 $0$분(이산 파트, $P(X=0) > 0$)이며, 주차를 한 차량들의 주차 시간은 연속적인 실수 범위(연속 파트)를 가짐.
* **누적분포함수 (CDF) 구조**:
    * 혼합 확률 변수의 CDF는 항상 이산형 CDF와 연속형 CDF의 볼록 결합(Convex Combination)으로 쪼개어 나타낼 수 있음.
        $$F_X(x) = a F_{\text{discrete}}(x) + (1-a) F_{\text{continuous}}(x) \quad (0 < a < 1)$$
    * **시각적 형태**: 그래프를 그리면, 완만하게 상승하는 곡선(연속형 특징) 중간중간에 특정 값 $x_j$ 지점에서 수직으로 점프하는 불연속 계단(이산형 특징)이 결합된 형태를 보임.
* **기댓값의 일반 계산법**:
    * 이산 파트와 연속 파트를 각각 나누어 계산한 뒤 결합함.
        $$E[X] = a E[X_{\text{discrete}}] + (1-a) E[X_{\text{continuous}}]$$

---

## 2. 디랙 델타 함수 (Dirac Delta Function, $\delta(x)$)
* **정의**: 수학적으로 엄밀한 의미의 함수는 아니며, 분포(Distribution) 또는 일반화된 함수(Generalized Function)임.
    * $x=0$이 아닌 모든 곳에서 $0$의 값을 가짐.
        $$\delta(x) = 0 \quad (\text{단, } x \ne 0)$$
    * $x=0$ 지점에서는 무한대($\infty$)로 솟구치며, 전체 적분 면적은 정확히 $1$이 됨.
        $$\int_{-\infty}^{\infty} \delta(x) \, dx = 1$$

* **단위계단함수 (Unit Step Function, $u(x)$) 와의 관계**:
    * 단위계단함수는 다음과 같이 정의됨.
        $$u(x) = \begin{cases} 1 & x \ge 0 \\ 0 & x < 0 \end{cases}$$
    * 이 함수는 $x=0$에서 급격한 점프(미분 불가능)가 일어나는데, 일반화된 미분을 도입하면 도함수가 바로 디랙 델타 함수가 됨.
        $$\frac{d}{dx} u(x) = \delta(x)$$

* **체 거르기 성질 (Sifting Property)**:
    * 임의의 연속함수 $g(x)$에 대해, 델타 함수를 곱해 적분하면 델타 함수가 솟구친 $x_0$ 지점에서의 함숫값만을 쏙 빼내어(체로 걸러내듯) 반환해 줌.
        $$\int_{-\infty}^{\infty} g(x) \delta(x - x_0) \, dx = g(x_0)$$

---

## 3. 델타 함수를 이용한 혼합 변수의 PDF 표현
* **문제의 발단**: 혼합형 CDF는 불연속 점프 지점이 존재하므로 미분이 불가능하여 기존 수학 체계에서는 하나의 깔끔한 PDF로 나타낼 수 없음.
* **해결책 (일반화된 PDF, Generalized PDF)**:
    * 디랙 델타 함수를 도입하면 점프가 발생하는 이산 지점들을 임펄스(Impulse) 성분으로 표현하여 전체 구간에서 정의되는 하나의 일반화된 PDF $f_X(x)$를 얻을 수 있음.
    * **표현 공식**:
        $$f_X(x) = f_{\text{active}}(x) + \sum_{j} P(X = x_j) \delta(x - x_j)$$
        * $f_{\text{active}}(x)$: 연속적인 부분의 확률 밀도 (CDF의 기울기)
        * $P(X = x_j)$: $x_j$ 지점에서의 이산 확률 크기 (CDF의 수직 점프 높이)
* **LOTUS를 통한 기댓값 계산의 단순화**:
    * 델타 함수를 사용해 일반화된 PDF를 구축해두면, 기댓값을 구할 때 이산형과 연속형을 따로 쪼개어 계산할 필요 없이 **오직 단 한 번의 적분 연산**만으로 통합 해결할 수 있음.
        $$E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) \, dx$$
        *(적분 계산 도중 델타 함수 항들은 Sifting Property에 의해 대수적인 덧셈 값으로 자동 치환됨)*

---

## 4. Detailed Solutions for Chapter 4.10 ~ 4.12 Examples

### **Example 4.7 (혼합 확률 변수의 CDF 분석과 기댓값)**
**[Problem]**
Let $X$ be a mixed random variable with CDF given by:
$$F_X(x) = \begin{cases} 0 & x < 0 \\ \frac{1}{2} + \frac{x}{4} & 0 \le x < 2 \\ 1 & x \ge 2 \end{cases}$$
1. Find the probability of the discrete jumps, $P(X = 0)$ and $P(X = 2)$.
2. Express the generalized PDF of $X$, $f_X(x)$, using the Dirac delta function.
3. Find the expected value $E[X]$.

---

**[Solution]**

#### 1. 이산 점프 확률 구하기
CDF 그래프에서 수직 점프가 일어나는 불연속 지점을 찾음.
* **$x = 0$ 지점**:
    * $F_X(0^-) = 0$
    * $F_X(0) = \frac{1}{2} + 0 = \frac{1}{2}$
    * 점프 높이: $P(X = 0) = F_X(0) - F_X(0^-) = \frac{1}{2} - 0 = \frac{1}{2}$
* **$x = 2$ 지점**:
    * $F_X(2^-) = \frac{1}{2} + \frac{2}{4} = 1$
    * $F_X(2) = 1$
    * 점프 높이: $P(X = 2) = F_X(2) - F_X(2^-) = 1 - 1 = 0$ (즉, $x=2$ 지점에서는 실제 점프가 일어나지 않고 매끄럽게 $1$에 도달한 연속 지점임)
* **정답**: $P(X = 0) = \frac{1}{2}$, $P(X = 2) = 0$ 임.

#### 2. 일반화된 PDF $f_X(x)$ 유도
* **연속 파트 $f_{\text{active}}(x)$**: $0 < x < 2$ 구간에서 CDF를 미분함.
    $$f_{\text{active}}(x) = \frac{d}{dx} \left( \frac{1}{2} + \frac{x}{4} \right) = \frac{1}{4}$$
* **이산 파트 (임펄스)**: $x=0$ 지점에서 점프 높이 $\frac{1}{2}$ 만큼의 델타 성분이 존재함.
    $$\text{Impulse Part} = \frac{1}{2} \delta(x)$$
* **종합**:
    $$f_X(x) = \frac{1}{4} [u(x) - u(x-2)] + \frac{1}{2} \delta(x)$$
    *(구간 외에서는 $0$이므로 윈도우 함수 성분 $u(x) - u(x-2)$를 곱해 나타냄)*
* **정답**: $f_X(x) = \frac{1}{4} + \frac{1}{2}\delta(x) \quad (0 < x < 2$ 구간 및 $x=0$ 임펄스 포함) 임.

#### 3. 기댓값 $E[X]$ 계산
일반화된 PDF를 LOTUS 공식에 넣어 전체 적분을 수행함.
$$E[X] = \int_{-\infty}^{\infty} x f_X(x) \, dx = \int_{0}^{2} x \cdot \left(\frac{1}{4}\right) \, dx + \int_{-\infty}^{\infty} x \cdot \left(\frac{1}{2}\delta(x)\right) \, dx$$
* **첫 번째 항 (연속 파트 적분)**:
    $$\int_{0}^{2} \frac{x}{4} \, dx = \left[ \frac{x^2}{8} \right]_{0}^{2} = \frac{4}{8} - 0 = \frac{1}{2}$$
* **두 번째 항 (이산 파트 적분 - Sifting Property 적용)**:
    $$\int_{-\infty}^{\infty} \frac{1}{2} x \delta(x) \, dx = \frac{1}{2} \cdot (0) = 0 \quad (\because x=0 \text{ 대입})$$
* **종합**:
    $$E[X] = \frac{1}{2} + 0 = \frac{1}{2} = 0.5$$
* **정답**: 기댓값 $E[X] = 0.5$ 임.
*(물리적으로 평균을 생각해보면, 절반의 확률로 $0$을 얻고 나머지 절반의 확률로는 $[0, 2]$ 구간의 평균값인 $1$을 얻으므로, 전체 평균은 $0(0.5) + 1(0.5) = 0.5$가 됨을 확인할 수 있음)*
