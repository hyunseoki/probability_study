# 📖 Chapter 1.3: Random Experiments and Probabilities — Summary

*Textbook Chapter Link: [Chapter 1.3: Random Experiments and Probabilities](https://www.probabilitycourse.com/chapter1/1_3_0_random_experiments.php)*

이 장(Chapter)은 무작위 실험의 수학적 정의, 확률의 3대 공리, 그리고 표본 공간의 종류(이산/연속)에 따른 확률 모델의 분류와 계산법을 다룸.

---

## 1. 무작위 실험과 사건 (Random Experiments & Events)
* **무작위 실험 (Random Experiment)**: 결과를 확실하게 예측할 수 없는 관찰이나 실험 과정임.
* **시행 (Trial)**: 무작위 실험을 단 한 번 구체적으로 실행하는 행위임. (예: 동전을 1번 던지는 행위)
* **결과 (Outcome, $s$ 또는 $\omega$)**: 무작위 실험(또는 1회의 시행)을 통해 얻은 구체적인 개별 결과임. (표본 공간의 원소이므로 $s \in S$ 또는 $\omega \in \Omega$ 로 표기함)
* **표본 공간 (Sample Space, $S$ 또는 $\Omega$)**: 발생 가능한 모든 결과(Outcomes, $s$)들의 집합임. 집합론의 전체집합에 해당함.
* **사건 (Event)**: 확률을 부여할 수 있는 표본 공간 $S$의 부분집합임.
    * **사건의 발생 (Occurrence)**: 실험의 실제 결과(Outcome, $s$)가 사건 집합 $E$의 원소일 때, **"사건 $E$가 발생했다"**고 정의함. ($s \in E$ 임을 의미함)
    * *예시*: 주사위를 던져 짝수가 나오는 사건 $E = \{2, 4, 6\}$일 때, 던져서 나온 눈(Outcome, $s$)이 $4$라면 사건 $E$가 발생한 것임 ($4 \in E$).
    * **사건의 집합 연산**: 사건은 집합이므로, Union and Intersection 연산이 적용됨.

---

## 2. 확률의 공리 (Axioms of Probability)
러시아 수학자 콜모고로프(Kolmogorov)가 정립한 확률의 3대 공리임.

### 확률 함수 (Probability Function / Measure, $P$)의 정의
* **확률 함수 (Probability Function / Measure, $P$)**: 표본 공간 $S$의 사건(집합)을 입력받아 $0$과 $1$ 사이의 실수를 반환하는 함수이면서, 아래의 **콜모고로프 3대 공리(Kolmogorov's Axioms)**를 만족하는 함수임.
    * **정의역 (Domain)**: 표본 공간 $S$의 부분집합(사건)들의 집합인 사건 공간(Event Space, $\mathcal{F}$)임.
    * **공역 (Codomain)**: $[0, 1]$ 범위의 실수임.
    * **기호 표현**: $P : \mathcal{F} \rightarrow [0, 1]$
    * *주의*: 개별 결과(Outcome, $s \in S$)가 아니라 **결과들의 집합인 사건(Event, $E \subset S$)을 입력**으로 받음. (예: 주사위 눈 2가 나오는 확률을 구할 때 $P(2)$가 아니라 집합 기호를 씌운 $P(\{2\})$가 정확한 표현임)

### 확률론의 주요 표기법 (Probability Notation Summary)
* **교집합 (Intersection / And)**: 사건 $A$와 $B$가 동시에 발생할 확률 (쉼표 `,` 또는 병렬 표기 $AB$로 자주 축약함)
    $$P(A \cap B) = P(A \text{ and } B) = P(A, B) = P(AB)$$
* **합집합 (Union / Or)**: 사건 $A$ 또는 $B$가 발생할 확률
    $$P(A \cup B) = P(A \text{ or } B)$$
* **차집합 (Difference)**: 사건 $A$에서 $B$를 제외한 사건의 확률
    $$P(A \setminus B) = P(A - B) = P(A \cap B^c)$$
* **여집합 (Complement / Not)**: 사건 $A$가 발생하지 않을 확률
    $$P(A^c) = P(A') = P(\bar{A})$$

### 콜모고로프의 확률 3대 공리 (Kolmogorov's Axioms)
* **공리 1. 비음수성 (Non-negativity)**: 모든 사건 $A$에 대해 확률은 $0$보다 크거나 같음.
    $$P(A) \ge 0$$
* **공리 2. 규격화 (Normalization)**: 표본 공간(전체집합) $S$의 확률은 $1$임.
    $$P(S) = 1$$
* **공리 3. 가산 가법성 (Countable Additivity)**: 서로소(Disjoint / Mutually Exclusive)인 사건들 $A_1, A_2, A_3, \dots$에 대해, 이들의 합집합 확률은 각 사건 확률의 합과 같음.
    $$P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$
    *(유한한 개수의 서로소 사건들에 대해서도 동일하게 성립함: $P(A \cup B) = P(A) + P(B)$)*

---

## 3. 확률의 주요 성질 (Properties of Probability)
위의 3대 공리로부터 수학적으로 유도되는 핵심 성질들임.

* **성질 1. 여사건의 확률 (Complement Rule)**:
    $$P(A^c) = 1 - P(A)$$
    *(유도: $A \cap A^c = \emptyset$ 이고 $A \cup A^c = S$ 이므로, 공리 2와 3에 의해 $P(A) + P(A^c) = P(S) = 1$이 됨)*

* **성질 2. 공집합의 확률 (Probability of Empty Set)**:
    $$P(\emptyset) = 0$$
    *(유도: $S^c = \emptyset$ 이므로, 성질 1에 의해 $P(\emptyset) = P(S^c) = 1 - P(S) = 1 - 1 = 0$이 됨)*

* **성질 3. 단조성 (Monotonicity)**:
    $$A \subset B \implies P(A) \le P(B)$$
    *(유도: $B = A \cup (B \setminus A)$ 이고 두 집합은 서로소이므로, $P(B) = P(A) + P(B \setminus A)$가 됨. 공리 1에 의해 $P(B \setminus A) \ge 0$이므로 $P(B) \ge P(A)$가 성립함)*

* **성질 4. 확률의 상한선**:
    모든 사건 $A$에 대해 확률은 $1$보다 작거나 같음.
    $$P(A) \le 1$$
    *(유도: $A \subset S$ 이므로 단조성(성질 3)과 공리 2에 의해 $P(A) \le P(S) = 1$이 됨)*

* **성질 5. 차집합의 확률**:
    $$P(A \setminus B) = P(A) - P(A \cap B)$$
    *(유도: $A = (A \setminus B) \cup (A \cap B)$ 이고 두 집합은 서로소이므로, $P(A) = P(A \setminus B) + P(A \cap B)$가 됨)*

* **성질 6. 포함-배제의 원리 (Inclusion-Exclusion Principle)**:
    $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
    *(유도: $A \cup B = (A \setminus B) \cup B$ 이고 두 집합은 서로소이므로, $P(A \cup B) = P(A \setminus B) + P(B)$임. 여기에 성질 5를 대입하면 유도됨)*

---

## 4. 이산 확률 모델 (Discrete Probability Models)
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

## 5. 연속 확률 모델 (Continuous Probability Models)
* **정의**: 표본 공간 $S$가 **비가산 집합(Uncountable Set)**인 경우임. (예: 실수 구간 $S = [0, 1]$ 등)
* **특징**:
    1. **개별 결과의 확률은 $0$임**: 연속형 모델에서는 어떤 특정 결과 $x \in S$ 하나가 정확히 일어날 확률은 항상 $0$임.
     $$P(x) = P(\{x\}) = 0 \quad (\text{모든 } x \in S \text{에 대해})$$
     * *이유 (직관)*: 구간을 무한히 쪼갤 때, 균등한(Uniform) 확률을 가진 미소 구간의 크기는 $0$으로 수렴하기 때문에 그 내부의 단일점 확률 역시 $0$이 됨.
    2. **확률은 구간의 길이/면적에 비례함**: 개별 점의 확률은 $0$이지만, 특정 구간(Interval)에 속할 확률은 의미 있는 양수(Positive Real Number) 값을 가짐.
    3. **적분(Integration)의 필요성**: 이산형처럼 단순 합(Summation)을 쓸 수 없으므로, 연속 확률 모델에서는 적분을 통해 확률을 계산함. (추후 확률변수 파트에서 PDF를 통해 구체적으로 학습하게 됨)

---

## 6. 대표 예제 해설 (Example Problems)

### Example 1 (Disjoint Case): 대통령 선거 예제
**[Problem]**
대통령 선거에 후보 A, B, C, D가 출마함. 여론조사 결과 A가 당선될 확률은 20%, B가 당선될 확률은 40%임. 이때 A 또는 B가 당선될 확률은?

**[Solution]**

* **1단계 ($S$)**: 후보 A, B, C, D가 이기는 개별 결과를 $a, b, c, d$라 하면, $S = \{a, b, c, d\}$ 임.
* **2단계 ($E$)**:
    * A가 이길 사건: $E_A = \{ s \in S \mid s\text{는 A가 이기는 결과} \} = \{a\} \quad [P(E_A) = 0.2]$
    * B가 이길 사건: $E_B = \{ s \in S \mid s\text{는 B가 이기는 결과} \} = \{b\} \quad [P(E_B) = 0.4]$
* **3단계 (Relation)**: 단 한 명만 당선될 수 있으므로 두 사건은 공통 원소가 없음.
    $$E_A \cap E_B = \{a\} \cap \{b\} = \emptyset \quad (\text{Disjoint})$$
* **4단계 (Calculate)**: 서로소이므로 **공리 3 (가산 가법성)**을 대입함.
    $$P(E_A \cup E_B) = P(E_A) + P(E_B) = 0.2 + 0.4 = 0.6 \quad (60\%)$$

---

### Example 2 (Complement / Intersection Case): 오늘과 내일의 비 예제
**[Problem]**
오늘 비가 올 확률은 $60\%$, 내일 비가 올 확률은 $50\%$이며, 이틀 모두 비가 오지 않을 확률은 $30\%$임. 오늘 또는 내일 비가 올 확률을 구하시오.

**[Solution]**

* **1단계 ($S$)**: 이틀간 날씨를 관찰하므로 개별 결과 $s$는 (오늘 날씨, 내일 날씨)의 조합(2-튜플)임.
    $$S = \{ s \mid s\text{는 (오늘 날씨, 내일 날씨)의 조합} \}$$
    *(이때 $s$는 $(\text{비}, \text{비})$, $(\text{비}, \text{비 안 옴})$ 등의 4가지 원소 중 하나임)*

* **2단계 ($E$)**:
    * 오늘 비가 올 사건: $A = \{ s \in S \mid s\text{의 오늘 날씨가 비임} \} \quad [P(A) = 0.6]$
    * 내일 비가 올 사건: $B = \{ s \in S \mid s\text{의 내일 날씨가 비임} \} \quad [P(B) = 0.5]$
    * 이틀 모두 비가 오지 않을 사건: $(A \cup B)^c = A^c \cap B^c = \{ s \in S \mid s\text{의 오늘과 내일 날씨 모두 비가 아님} \} \quad [P((A \cup B)^c) = 0.3]$
* **3단계 (Relation)**: "오늘 비 또는 내일 비($A \cup B$)"와 "이틀 다 비 안 옴($(A \cup B)^c$)"은 정확히 여집합 관계임.
    $$(A \cup B) \cap (A \cup B)^c = \emptyset$$
* **4단계 (Calculate)**: 여사건 성질을 적용하여 합집합 확률을 구함.
    $$P(A \cup B) = 1 - P((A \cup B)^c) = 1 - 0.3 = 0.7 \quad (70\%)$$

---

### Example 3 (Discrete Model - Countably Infinite): 무한 가산 표본 공간의 도박 게임
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

### Example 4 (Discrete Model - Equally Likely): 공정한 주사위 두 번 던지기
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

---

### Example 5 (Continuous Model): 버스 도착 시간 문제
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
