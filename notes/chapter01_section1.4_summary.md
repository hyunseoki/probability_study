# 📖 Chapter 1.4: Discrete & Continuous Probability Models — Summary

*Textbook Chapter Links: [1.3.4 Discrete Models](https://www.probabilitycourse.com/chapter1/1_3_4_discrete_models.php) & [1.3.5 Continuous Models](https://www.probabilitycourse.com/chapter1/1_3_5_continuous_models.php)*

이 장(Chapter)은 표본 공간(Sample Space, $S$)의 기수(Cardinality)에 따라 확률 모델(Probability Model)을 이산(Discrete)과 연속(Continuous)으로 분류하고, 각각의 확률 계산법과 물리적 직관을 다룸.

---

## 1. 이산 확률 모델 (Discrete Probability Models)
* **정의**: 표본 공간 $S$가 **가산 집합(Countable Set)**인 경우임. 즉, $S = \{s_1, s_2, s_3, \dots\}$와 같이 모든 결과(Outcomes)들을 셀 수 있는 형태임.
* **확률 계산**: 개별 결과 하나만 가지는 낱개 집합(근원사건, Singleton Set $\{s_j\}$)들끼리는 항상 **서로소(Disjoint)** 관계임. (한 번의 시행에서 서로 다른 두 결과가 동시에 발생할 수는 없기 때문)
  따라서 사건 $A \subset S$의 확률은 서로소인 낱개 집합들의 합집합 확률과 같으므로, **확률의 공리 3 (가산 가법성)**에 의해 개별 결과들의 확률의 합(Summation)으로 계산됨.
  $$P(A) = P\left(\bigcup_{s_j \in A} \{s_j\}\right) = \sum_{s_j \in A} P(s_j)$$

* **특징**: 이산 모델에서는 개별 결과의 확률 $P(s_j)$를 모두 더해 사건의 확률을 구하며, 전체 결과의 확률 합은 항상 $1$이 됨 ($\sum_{s_j \in S} P(s_j) = 1$).

### 동일한 확률을 가진 유한 표본 공간 (Finite Sample Spaces with Equally Likely Outcomes)
* **정의**: 표본 공간 $S = \{s_1, s_2, \dots, s_N\}$가 유한 집합(Finite Set)이고, 모든 개별 결과들의 발생 확률이 동일한 경우임.
  $$P(s_i) = P(s_j) = \frac{1}{N} \quad (\text{모든 } i, j \in \{1, 2, \dots, N\})$$
* **확률 계산**: 이 경우 임의의 사건 $A \subset S$의 확률은 단순히 사건 $A$의 원소 개수(Cardinality)를 표본 공간 $S$의 원소 개수로 나누는 **개수 세기 문제(Counting Problem)**로 귀결됨.
  $$P(A) = \frac{|A|}{|S|}$$

---

## 2. 연속 확률 모델 (Continuous Probability Models)
* **정의**: 표본 공간 $S$가 **비가산 집합(Uncountable Set)**인 경우임. (예: 실수 구간 $S = [0, 1]$ 등)
* **특징**:
  1. **개별 결과의 확률은 $0$임**: 연속형 모델에서는 어떤 특정 결과 $x \in S$ 하나가 정확히 일어날 확률은 항상 $0$임.
     $$P(x) = P(\{x\}) = 0 \quad (\text{모든 } x \in S \text{에 대해})$$
     * *이유 (직관)*: 구간을 무한히 쪼갤 때, 균등한(Uniform) 확률을 가진 미소 구간의 크기는 $0$으로 수렴하기 때문에 그 내부의 단일점 확률 역시 $0$이 됨.
  2. **확률은 구간의 길이/면적에 비례함**: 개별 점의 확률은 $0$이지만, 특정 구간(Interval)에 속할 확률은 의미 있는 양수(Positive Real Number) 값을 가짐.
  3. **적분(Integration)의 필요성**: 이산형처럼 단순 합(Summation)을 쓸 수 없으므로, 연속 확률 모델에서는 적분을 통해 확률을 계산함. (추후 확률변수 파트에서 PDF를 통해 구체적으로 학습하게 됨)

---

## 3. 대표 예제 해설 (Example Problems)

### Example 1 (Discrete Model): 무한 가산 표본 공간의 도박 게임
**[Problem]**
도박 게임에서 어떤 자연수 $k \in \mathbb{N}$에 대해 확률 $\frac{1}{2^k}$로 $k-2$ 달러를 얻는다고 함.
1. 이 확률 모델이 유효한(Valid) 확률 측도인지 확인하시오.
2. $1$달러 이상 $4$달러 미만으로 딸 확률을 구하시오.
3. $2$달러 초과로 딸 확률을 구하시오.

**[Solution]**
1. **표본 공간 및 확률 측도 검증**:
   * 얻는 금액(Outcomes)을 $k$로 나타내면 표본 공간 $S = \{-1, 0, 1, 2, 3, \dots\}$이며, 이는 가산 무한집합임.
   * 각 결과의 확률은 $P(k) = \frac{1}{2^{k+2}}$ 임 (예: $k=-1$일 때 $P(-1) = 1/2$, $k=0$일 때 $P(0) = 1/4$, $k=1$일 때 $P(1) = 1/8$, $\dots$).
   * 전체 확률의 합이 $1$인지 기하급수(Geometric Series)의 합으로 확인:
     $$\sum_{k=-1}^{\infty} P(k) = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots = \frac{1/2}{1 - 1/2} = 1$$
     따라서 유효한 확률 측도임.

2. **$1$달러 이상 $4$달러 미만으로 딸 사건 $A$**:
   * $A = \{1, 2, 3\}$
   * $P(A) = P(1) + P(2) + P(3) = \frac{1}{8} + \frac{1}{16} + \frac{1}{32} = \frac{7}{32} \approx 0.219$

3. **$2$달러 초과로 딸 사건 $B$**:
   * $B = \{3, 4, 5, \dots\}$
   * 여사건 규칙(Complement Rule)을 적용하여 계산:
     $$P(B) = 1 - P(B^c) = 1 - P(\{-1, 0, 1, 2\})$$
     $$P(B) = 1 - \left(\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16}\right) = 1 - \frac{15}{16} = \frac{1}{16} = 0.0625$$

---

### Example 2 (Continuous Model): 버스 도착 시간 문제
**[Problem]**
버스가 시간 구간 $[1, 2)$ 사이의 임의의 실수 시각에 균등하게(Uniformly) 도착한다고 함. 
1. 도착 시각 $T$가 정확히 $1.5$가 될 확률 $P(1.5)$를 구하시오.
2. 버스가 시각 $1$과 $1.5$ 사이에 도착할 확률 $P([1, 1.5))$를 구하시오.
3. 임의의 시각 $1 \le a \le b < 2$에 대해 $P(a \le T \le b)$를 구하시오.

**[Solution]**
1. **정확한 단일 시점 도착 확률**:
   * 균등성(Uniformity)에 의해 구간 $[1, 2)$를 $2N+1$개의 동일한 크기의 부분 구간으로 쪼개면, 각각의 미소 구간 $A_N$의 확률은 $\frac{1}{2N+1}$이 됨.
   * 임의의 $N$에 대해 시각 $1.5$는 한 부분 구간 $A_N$에 속하므로 $\{1.5\} \subset A_N$이 성립함.
   * 따라서 단조성(Monotonicity)에 의해 $P(1.5) \le P(A_N) = \frac{1}{2N+1}$ 임.
   * $N \to \infty$로 보낼 때 $\frac{1}{2N+1} \to 0$ 이므로, $P(1.5) = 0$ 이 됨.

2. **$1$시에서 $1.5$시 사이에 도착할 확률**:
   * 표본 공간 $S = [1, 2)$ 이고, 균등성(Uniformity)에 의해 $P([1, 1.5)) = P([1.5, 2))$ 임.
   * $P([1, 1.5)) + P([1.5, 2)) = P(S) = 1$ 이므로, $P([1, 1.5)) = 0.5$ 임.

3. **임의의 구간 $[a, b]$에 속할 확률**:
   * 균등 분포(Uniform Distribution)에서 확률은 구간의 길이에 비례함. 전체 표본 공간의 길이가 $2 - 1 = 1$이고 전체 확률이 $1$이므로, 구간 $[a, b]$의 확률은 그 구간의 길이 자체와 같음.
   * $P(a \le T \le b) = b - a$

---

### Example 3 (Discrete Model - Equally Likely Outcomes): 공정한 주사위 두 번 던지기
**[Problem]**
공정한 주사위를 두 번 던져 첫 번째 결과를 $X_1$, 두 번째 결과를 $X_2$라 할 때, 두 결과의 합이 8이 될 확률($X_1 + X_2 = 8$)을 구하시오. (단, 모든 결과는 동일한 확률로 발생함)

**[Solution]**
* **1단계 ($S$)**: 개별 결과 $s$는 (첫 번째 눈, 두 번째 눈)의 2-튜플 조합임.
  $$S = \{ (i, j) \mid i, j \in \{1, 2, 3, 4, 5, 6\} \} \implies |S| = 6 \times 6 = 36$$
  (각 결과 $s \in S$의 발생 확률은 $\frac{1}{36}$로 모두 동일함)
* **2단계 ($E$)**: 두 결과의 합이 8이 되는 사건 $A$를 정의함.
  $$A = \{ s \in S \mid X_1 + X_2 = 8 \} = \{(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)\} \implies |A| = 5$$
  *(참고: 주사위의 순서가 다르므로 $(2, 6)$과 $(6, 2)$는 서로 다른 별개의 Outcomes로 취급함)*
* **3단계 (Relation)**: 단일 사건의 확률 계산이므로 생략.
* **4단계 (Calculate)**: 모든 Outcomes가 동일한 확률을 가지므로 공식 $P(A) = \frac{|A|}{|S|}$를 대입하여 계산함.
  $$P(A) = \frac{5}{36}$$
