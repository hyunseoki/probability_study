# 📖 Chapter 5.2: Two Continuous Random Variables — Summary

*Textbook Chapter Link: [Chapter 5.2: Two Continuous Random Variables](https://www.probabilitycourse.com/chapter5/5_2_0_continuous_vars.php)*

이 장은 두 개의 연속확률변수가 함께 정의될 때의 수학적 분석 기법(결합 PDF/CDF, 주변 분포, 조건부 밀도함수, 독립성, 그리고 다차원 변수 변환 및 Jacobian법)을 요약 정리함.

---

## 1. 결합 PDF와 주변 PDF (Joint PDF & Marginal PDF)
* **결합 확률밀도함수 (Joint Probability Mass Function, $f_{X,Y}(x,y)$)**:
    * 두 연속형 확률변수 $X$와 $Y$의 분포 영역과 확률 집중도를 이변수 함수로 나타낸 것임.
    * 특정 평면 영역 $A$에 속할 확률은 결합 PDF의 중적분(부피)으로 정의됨.
        $$P((X,Y) \in A) = \iint_{A} f_{X,Y}(x,y) \, dx \, dy$$
    * **성질**:
        1. 비음성: $f_{X,Y}(x,y) \ge 0 \quad (\text{모든 } x, y \in \mathbb{R})$
        2. 총 부피는 1: $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x,y) \, dx \, dy = 1$
* **주변 확률밀도함수 (Marginal PDF)**:
    * 상대방 변수의 전체 영역($-\infty$부터 $\infty$까지)에 대해 결합 PDF를 적분(소거)하여 구함.
        $$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) \, dy, \qquad f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) \, dx$$

---

## 2. 결합 CDF (Joint CDF)
* **결합 누적분포함수 (Joint CDF, $F_{X,Y}(x,y)$)**:
    * 두 변수 $X, Y$가 각각 $x, y$ 이하일 누적 확률을 나타내며, 중적분으로 표현됨.
        $$F_{X,Y}(x,y) = P(X \le x, Y \le y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f_{X,Y}(u,v) \, dv \, du$$
* **주변 CDF**: 한쪽 변수의 경계를 무한대($\infty$)로 보낸 결과임.
    $$F_X(x) = F_{X,Y}(x, \infty), \qquad F_Y(y) = F_{X,Y}(\infty, y)$$
* **편미분을 통한 PDF 유도**:
    결합 CDF를 두 변수 $x$와 $y$에 대해 각각 한 번씩 편미분하면 결합 PDF를 얻음.
    $$f_{X,Y}(x,y) = \frac{\partial^2}{\partial x \partial y} F_{X,Y}(x,y)$$

---

## 3. 조건부 분포와 독립성 (Conditioning & Independence)
* **조건부 PDF (Conditional PDF, $f_{X|Y}(x|y)$)**:
    * $Y = y$라는 사건이 주어졌을 때 $X$의 확률밀도분포를 의미하며, 결합 PDF를 $Y$의 주변 PDF로 나누어 정의함.
        $$f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)} \quad (\text{단, } f_Y(y) > 0)$$
* **연속형 변수의 독립성 (Independence)**:
    * 두 연속형 확률변수 $X$와 $Y$가 서로 독립이라는 것은, 모든 $x, y$에 대해 결합 PDF가 주변 PDF의 곱으로 분리됨을 뜻함.
        $$f_{X,Y}(x,y) = f_X(x)f_Y(y) \quad \Longleftrightarrow \quad f_{X|Y}(x|y) = f_X(x)$$

---

## 4. 두 연속확률변수의 함수 변환 (Functions of Two Continuous RVs)
이변수 변환 $Z = g(X,Y)$ 또는 다차원 변환 $(U, V) = (g_1(X,Y), g_2(X,Y))$ 의 분포를 유도하는 방법임.

### (1) 누적분포함수법 (CDF Method)
단일 변수 $Z = g(X,Y)$의 분포를 구할 때 주로 사용되며, 중적분을 활용해 누적 영역의 확률을 구한 뒤 미분함.
1. $F_Z(z) = P(g(X,Y) \le z) = \iint_{g(x,y) \le z} f_{X,Y}(x,y) \, dx \, dy$ 식을 세워 적분 계산함.
2. 미분을 수행함: $f_Z(z) = \frac{d}{dz} F_Z(z)$.

### (2) 다차원 Jacobian 변환 공식 (Transformation Method)
두 변수 $X, Y$가 $U = g_1(X,Y)$, $V = g_2(X,Y)$로 일대일 대응 매핑(Inverse mapping $X = h_1(U,V), Y = h_2(U,V)$가 유일하게 존재)될 때 결합 PDF를 즉시 구하는 공식임.
$$f_{U,V}(u,v) = f_{X,Y}(h_1(u,v), h_2(u,v)) |J|$$
* **야코비안 (Jacobian, $J$)**:
    역상 매핑 함수들의 편도함수로 구성된 행렬식(Determinant)임.
    $$J = \det \begin{bmatrix} \frac{\partial h_1}{\partial u} & \frac{\partial h_1}{\partial v} \\ \frac{\partial h_2}{\partial u} & \frac{\partial h_2}{\partial v} \end{bmatrix} = \frac{\partial h_1}{\partial u}\frac{\partial h_2}{\partial v} - \frac{\partial h_1}{\partial v}\frac{\partial h_2}{\partial u}$$

---

## 5. Solved Problems (5.2 연습문제)

### **Example 5.2 (중적분 영역 확률 계산)**
**[Problem]**
Let $X$ and $Y$ be jointly continuous random variables with joint PDF:
$$f_{X,Y}(x,y) = \begin{cases} x + y & 0 < x, y < 1 \\ 0 & \text{otherwise} \end{cases}$$
1. Find the marginal PDF of $X$, $f_X(x)$.
2. Find $P(X + Y \le 1)$.

---

**[Solution]**
1. **Marginal PDF $f_X(x)$ 구하기**: (정의역 $0 < x < 1$ 범위에서 $y$에 대해 적분)
    $$f_X(x) = \int_{0}^{1} (x+y) \, dy = \left[ xy + \frac{1}{2}y^2 \right]_{0}^{1} = x + \frac{1}{2}$$
    * **정답**: $f_X(x) = \begin{cases} x + \frac{1}{2} & 0 < x < 1 \\ 0 & \text{otherwise} \end{cases}$ 임.
2. **$P(X+Y \le 1)$ 구하기**: (직각이등변삼각형 영역 $A = \{(x,y) \mid x+y \le 1, 0<x,y<1\}$ 상에서의 중적분)
    $$P(X + Y \le 1) = \int_{0}^{1} \int_{0}^{1-x} (x+y) \, dy \, dx$$
    * **안쪽 $y$ 적분**:
        $$\int_{0}^{1-x} (x+y) \, dy = \left[ xy + \frac{1}{2}y^2 \right]_{0}^{1-x} = x(1-x) + \frac{1}{2}(1-x)^2 = x - x^2 + \frac{1}{2} - x + \frac{1}{2}x^2 = \frac{1}{2} - \frac{1}{2}x^2$$
    * **바깥쪽 $x$ 적분**:
        $$\int_{0}^{1} \left( \frac{1}{2} - \frac{1}{2}x^2 \right) \, dx = \left[ \frac{1}{2}x - \frac{1}{6}x^3 \right]_{0}^{1} = \frac{1}{2} - \frac{1}{6} = \frac{1}{3}$$
    * **정답**: $P(X + Y \le 1) = \frac{1}{3}$ 임.
