# 📖 Chapter 4.5 ~ 4.6: Functions of Continuous Random Variables — Summary

*Textbook Chapter Link: [Chapter 4.5: Functions of Continuous RVs](https://www.probabilitycourse.com/chapter4/4_5_1_functions_continuous_rvs.php)*

이 장은 이미 알고 있는 연속확률변수 $X$를 임의의 함수에 입력하여 얻은 새로운 확률변수 $Y = g(X)$의 확률분포(PDF 및 CDF)를 유도하는 두 가지 핵심 기법(누적분포함수법, 일대일 대응 공식)을 요약 정리함.

---

## 1. 누적분포함수법 (The CDF Method)
* **정의**: 새로운 변수 $Y = g(X)$의 CDF를 먼저 구한 뒤, 이를 미분하여 PDF를 구하는 **가장 안전하고 만능으로 사용되는 표준 기법**임.
* **작동 단계 (4-Step Process)**:
    1. **정의 시작**: $Y$의 누적분포함수 정의식을 작성함.
        $$F_Y(y) = P(Y \le y) = P(g(X) \le y)$$
    2. **X의 영역으로 변환**: $g(X) \le y$ 부등식을 입력 변수 $X$에 대한 부등식 형태로 변형함. (이 단계에서 $g(x)$의 증가/감소 성질이 중요하게 쓰임)
    3. **X의 CDF 적용**: $X$에 대한 확률 식을 $X$의 CDF인 $F_X(\cdot)$로 표현함.
    4. **미분 수행**: 구한 $F_Y(y)$를 변수 $y$에 대해 미분하여 $Y$의 PDF를 얻음.
        $$f_Y(y) = \frac{d}{dy} F_Y(y)$$

* *장점*: $g(x)$가 일대일 대응이 아니거나(예: $Y = X^2$), 여러 구간에서 다르게 정의되는 불연속 함수인 경우에도 아무런 제약 없이 완벽하게 작동함.

---

## 2. 일대일 매핑 변환 공식 (One-to-One Mapping Formula)
* **사용 조건**:
    * 함수 $y = g(x)$가 확률변수 $X$의 치역 전체에서 **엄격한 단조함수(Strictly Monotonic)**(즉, 계속 증가하거나 계속 감소)여야 함.
    * 이 경우 일대일 대응이 성립하여 역함수 $x = g^{-1}(y)$가 유일하게 존재함.
    * $g(x)$와 그 역함수 $g^{-1}(y)$가 모두 미분 가능해야 함.
* **변환 공식**:
    $$f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right| = \frac{f_X(x)}{|g'(x)|} \quad (\text{단, } x = g^{-1}(y))$$

* **수학적 유도 (연쇄 법칙 활용)**:
    * $g(x)$가 증가함수일 때, $F_Y(y) = P(g(X) \le y) = P(X \le g^{-1}(y)) = F_X(g^{-1}(y))$ 임.
    * 합성함수의 미분법(Chain Rule)을 적용하여 양변을 $y$에 대해 미분하면:
        $$f_Y(y) = \frac{d}{dy} F_X(g^{-1}(y)) = F_X'(g^{-1}(y)) \cdot \frac{d}{dy} g^{-1}(y) = f_X(g^{-1}(y)) \cdot \frac{dx}{dy}$$
    * $g(x)$가 감소함수일 때는 부등호 방향이 바뀌어 음수 도함수가 생기며, 이를 합쳐 절댓값 기호 $|\cdot|$로 통일함으로써 위 공식이 유도됨.

* **야코비안 (Jacobian) 개념**:
    * 공식에서 $\left| \frac{dx}{dy} \right|$ 또는 $\frac{1}{|g'(x)|}$ 항은 1차원 야코비안에 해당함.
    * 이는 단순한 대수적 변환이 아니라, $X$ 축의 미소 구간 $dx$가 $Y$ 축의 미소 구간 $dy$로 변환될 때 발생하는 **공간의 스케일 변화율(넓이 보존 인자)**을 의미함.

---

## 3. 다대일 매핑 (Many-to-One Mapping)
* 만약 $y = g(x)$가 일대일 대응이 아닌 경우 (예: $Y = X^2$은 음수와 양수 영역 모두 양수로 매핑됨), 역함수의 해가 여러 개 존재함.
* **확장 공식**: $g(x_i) = y$를 만족시키는 서로 다른 실근 $x_1, x_2, \dots, x_m$이 존재할 때, 각 실근 지점에서의 공식들의 합으로 계산할 수 있음.
    $$f_Y(y) = \sum_{i=1}^{m} \frac{f_X(x_i)}{|g'(x_i)|}$$

---

## 4. Detailed Solutions for Chapter 4.5 ~ 4.6 Examples

### **Example 4.3 (일대일 변환 공식 — 선형 변환)**
**[Problem]**
Let $X$ be a continuous random variable with PDF $f_X(x)$. Let $Y = aX + b$ where $a \ne 0$ and $b$ are constants. Find the PDF of $Y$, $f_Y(y)$.

---

**[Solution]**

#### 1. 공식 조건 확인
$y = g(x) = ax + b$로 정의함.
* $a \ne 0$이므로 이 함수는 일대일 대응(직선)이며, 미분 가능한 단조함수임.
* 역함수 구하기: $y = ax + b \implies x = \frac{y-b}{a} \implies g^{-1}(y) = \frac{y-b}{a}$
* 역함수 미분: $\frac{d}{dy} g^{-1}(y) = \frac{1}{a}$
* 원래 함수 도함수: $g'(x) = a$

#### 2. 변환 공식 대입
공식 $f_Y(y) = f_X(g^{-1}(y)) \left| \frac{d}{dy} g^{-1}(y) \right|$ 에 대입함.
$$f_Y(y) = f_X\left(\frac{y-b}{a}\right) \left| \frac{1}{a} \right| = \frac{1}{|a|} f_X\left(\frac{y-b}{a}\right)$$
* **정답**: $f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y-b}{a}\right)$ 임.
*(이 공식은 정규분포의 표준화 및 복원 연산 시 기반이 되는 매우 중요한 공식임)*

---

### **Example 4.4 (다대일 변환 — 제곱 변환)**
**[Problem]**
Let $X$ be a continuous random variable with PDF $f_X(x)$. Let $Y = X^2$. Find the PDF of $Y$, $f_Y(y)$ for $y > 0$.

---

**[Solution]**

이 함수 $y = g(x) = x^2$은 $x$의 부호에 따라 일대일 대응이 아니므로 **CDF Method**를 적용함.

#### 1. CDF $F_Y(y)$ 설계 ($y > 0$ 일 때)
$$F_Y(y) = P(Y \le y) = P(X^2 \le y)$$
$y > 0$ 이므로 양변에 제곱근을 취하면 부등식은 다음과 같이 변형됨.
$$P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y})$$
이 확률은 $X$의 CDF로 다음과 같이 표현됨.
$$P(-\sqrt{y} \le X \le \sqrt{y}) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$$

#### 2. 양변을 $y$에 대해 미분하여 PDF 구하기
연쇄 법칙(Chain rule)을 활용해 $F_Y(y) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$ 를 미분함.
$$f_Y(y) = \frac{d}{dy} \left[ F_X(\sqrt{y}) - F_X(-\sqrt{y}) \right]$$
* **첫 번째 항 미분**:
    $$\frac{d}{dy} F_X(\sqrt{y}) = f_X(\sqrt{y}) \cdot \frac{d}{dy}(\sqrt{y}) = f_X(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}}$$
* **두 번째 항 미분**:
    $$\frac{d}{dy} F_X(-\sqrt{y}) = f_X(-\sqrt{y}) \cdot \frac{d}{dy}(-\sqrt{y}) = f_X(-\sqrt{y}) \cdot \left(-\frac{1}{2\sqrt{y}}\right)$$
* **종합**: (두 번째 항의 마이너스 마이너스가 만나 플러스가 됨)
    $$f_Y(y) = \frac{1}{2\sqrt{y}} \left[ f_X(\sqrt{y}) + f_X(-\sqrt{y}) \right]$$
* **정답**: $y > 0$ 일 때, $f_Y(y) = \frac{1}{2\sqrt{y}} \left[ f_X(\sqrt{y}) + f_X(-\sqrt{y}) \right]$ 이며, $y \le 0$ 일 때는 $f_Y(y) = 0$ 임.
