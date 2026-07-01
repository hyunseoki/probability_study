# 📖 Chapter 4.3: Mixed Random Variables — Summary

*Textbook Chapter Link: [Chapter 4.3: Mixed Random Variables](https://www.probabilitycourse.com/chapter4/4_3_1_mixed.php)*

이 장은 이산형 점프와 연속형 밀도가 결합된 혼합 확률 변수(Mixed Random Variable)의 수학적 취급법과, 이를 하나의 공식으로 통합하게 해주는 디랙 델타 함수(Dirac Delta Function)의 개념 및 응용을 요약 정리함.

---

## 1. 혼합 확률 변수 (Mixed Random Variables, 4.3.1)
* **정의**: 일부 구간에서는 연속적인 확률밀도를 갖고, 특정 개별 지점(Point)에서는 0보다 큰 이산 확률(점 질량, Point Mass)을 동시에 갖는 확률변수임.
* **CDF 구조**: 
    혼합형 CDF는 항상 이산형 CDF와 연속형 CDF의 볼록 결합(Convex Combination)으로 쪼개어 나타낼 수 있음.
    $$F_X(x) = a F_{\text{discrete}}(x) + (1-a) F_{\text{continuous}}(x) \quad (0 < a < 1)$$
    * **그래프 모양**: 연속적인 곡선으로 증가하는 도중, 특정 점 지점 $x_j$에서 수직으로 계단 모양 점프를 일으킴.
* **기댓값의 일반 계산법**:
    이산 파트와 연속 파트의 기댓값을 가중치를 곱해 합함.
    $$E[X] = a E[X_{\text{discrete}}] + (1-a) E[X_{\text{continuous}}]$$

---

## 2. 디랙 델타 함수 (Dirac Delta Function, $\delta(x)$, 4.3.2)
* **정의**: $x=0$인 지점에서 높이가 무한대($\infty$)가 되고, 그 외의 모든 지점에서는 $0$이 되며, 전체 적분 면적은 정확히 $1$이 되는 가상의 임펄스(Impulse) 함수임.
    $$\int_{-\infty}^{\infty} \delta(x) \, dx = 1$$
* **단위계단함수 (Unit Step Function, $u(x)$) 와의 관계**:
    * $u(x) = \begin{cases} 1 & x \ge 0 \\ 0 & x < 0 \end{cases}$ 의 도함수가 곧 델타 함수임.
        $$\frac{d}{dx} u(x) = \dots = \delta(x)$$
* **체 거르기 성질 (Sifting Property)**:
    임의의 연속함수 $g(x)$에 대해, 델타 함수를 곱한 적분은 $x_0$ 지점에서의 함숫값만을 반환함.
    $$\int_{-\infty}^{\infty} g(x) \delta(x - x_0) \, dx = g(x_0)$$

---

## 3. 일반화된 PDF (Generalized PDF)
* 혼합형 CDF는 점프 지점에서 미분이 불가능하여 통상적인 PDF를 가질 수 없으나, 델타 함수 성분을 도입하면 전 구간에서 정의되는 하나의 일반화된 PDF $f_X(x)$를 구축할 수 있음.
* **표현 공식**:
    $$f_X(x) = f_{\text{active}}(x) + \sum_{j} P(X = x_j) \delta(x - x_j)$$
    * $f_{\text{active}}(x)$: 연속적인 부분의 확률 밀도 (CDF의 기울기)
    * $P(X = x_j)$: 점프가 발생하는 지점 $x_j$에서의 이산 확률 크기 (점프 높이)
* **LOTUS 적용의 단순화**:
    일반화된 PDF를 활용하면, 기댓값을 구할 때 적분 기호 하나만으로 통일하여 해결할 수 있음.
    $$E[g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) \, dx$$

---

## 4. Solved Problems (4.3 연습문제)

### **Example 4.9**
**[Problem]**
Let $X$ be a mixed random variable with CDF:
$$F_X(x) = \begin{cases} 0 & x < 0 \\ \frac{1}{2} + \frac{x}{4} & 0 \le x < 2 \\ 1 & x \ge 2 \end{cases}$$
1. Find the probability of the discrete jumps, $P(X = 0)$ and $P(X = 2)$.
2. Write the generalized PDF $f_X(x)$ using the delta function.
3. Find $E[X]$.

---

**[Solution]**
1. **이산 점프 확률 구하기**:
    * $x=0$ 지점: $P(X=0) = F_X(0) - F_X(0^-) = \frac{1}{2} - 0 = \frac{1}{2}$
    * $x=2$ 지점: $P(X=2) = F_X(2) - F_X(2^-) = 1 - \left(\frac{1}{2} + \frac{2}{4}\right) = 1 - 1 = 0$ (실제 점프가 없고 연속인 점임)
2. **일반화된 PDF $f_X(x)$ 구하기**:
    * 연속 구간 ($0 < x < 2$) 미분: $f_{\text{active}}(x) = \frac{d}{dx} \left(\frac{1}{2} + \frac{x}{4}\right) = \frac{1}{4}$
    * $x=0$ 지점의 델타 임펄스 크기는 $\frac{1}{2}$ 임.
    * 따라서:
        $$f_X(x) = \frac{1}{4} [u(x) - u(x-2)] + \frac{1}{2} \delta(x)$$
3. **기댓값 $E[X]$ 구하기**:
    $$E[X] = \int_{0}^{2} x \cdot \left(\frac{1}{4}\right) \, dx + \int_{-\infty}^{\infty} x \cdot \left(\frac{1}{2} \delta(x)\right) \, dx$$
    * 첫 번째 적분: $\left[ \frac{x^2}{8} \right]_{0}^{2} = \frac{1}{2}$
    * 두 번째 적분 (Sifting property): $\frac{1}{2} \cdot (0) = 0$
    * 따라서: $E[X] = \frac{1}{2} + 0 = 0.5$
