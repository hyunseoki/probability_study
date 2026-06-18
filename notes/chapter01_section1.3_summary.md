# 📖 Chapter 1.3: Random Experiments and Probabilities — Summary

*Textbook Chapter Link: [Chapter 1.3: Random Experiments and Probabilities](https://www.probabilitycourse.com/chapter1/1_3_0_random_experiments.php)*

이 장은 무작위 실험의 수학적 정의, 확률의 3대 공리, 그리고 이 공리로부터 유도되는 확률의 주요 성질들을 다룸.

---

## 1. 무작위 실험과 사건 (Random Experiments & Events)
* **무작위 실험 (Random Experiment)**: 결과를 확실하게 예측할 수 없는 관찰이나 실험 과정임.
* **시행 (Trial)**: 무작위 실험을 단 한 번 구체적으로 실행하는 행위임. (예: 동전을 1번 던지는 행위)
* **결과 (Outcome, $s$ 또는 $\omega$)**: 무작위 실험(또는 1회의 시행)을 통해 얻은 구체적인 개별 결과임. (표본 공간의 원소이므로 $s \in S$ 또는 $\omega \in \Omega$ 로 표기함)
* **표본 공간 (Sample Space, $S$ 또는 $\Omega$)**: 발생 가능한 모든 결과(Outcomes, $s$)들의 집합임. 집합론의 전체집합에 해당함.
* **사건 (Event, $E$)**: 확률을 부여할 수 있는 표본 공간 $S$의 부분집합임.
  * **사건의 발생 (Occurrence)**: 실험의 실제 결과(Outcome, $s$)가 사건 집합 $E$의 원소일 때, **"사건 $E$가 발생했다"**고 정의함. ($s \in E$ 임을 의미함)
  * *예시*: 주사위를 던져 짝수가 나오는 사건 $E = \{2, 4, 6\}$일 때, 던져서 나온 눈(Outcome, $s$)이 $4$라면 사건 $E$가 발생한 것임 ($4 \in E$).
  * **사건의 집합 연산**: 사건은 집합이므로, Union and Intersection 연산이 적용됨.



---

## 2. 확률의 공리 (Axioms of Probability)

### 확률 함수 (Probability Function / Measure, $P$)의 정의
* **확률 함수 (Probability Function / Measure, $P$)**: 표본 공간 $S$의 사건(집합)을 입력받아 $0$과 $1$ 사이의 실수를 반환하는 함수이면서, 아래의 **콜모고로프 3대 공리(Kolmogorov's Axioms)**를 만족하는 함수임.
  * **정의역 (Domain)**: 표본 공간 $S$의 부분집합(사건)들의 집합인 사건 공간(Event Space, $\mathcal{F}$)임.
  * **공역 (Codomain)**: $[0, 1]$ 범위의 실수임.
  * **기호 표현**: $P : \mathcal{F} \rightarrow [0, 1]$
  * *주의*: 개별 결과(Outcome, $s \in S$)가 아니라 **결과들의 집합인 사건(Event, $E \subset S$)을 입력**으로 받음. (예: 주사위 눈 2가 나오는 확률을 구할 때 $P(2)$가 아니라 집합 기호를 씌운 $P(\{2\})$가 정확한 표현임)

### 확률론의 주요 표기법 (Probability Notation Summary)
교재 및 문제 풀이에서 자주 혼용되는 핵심 기호(Notation) 정리임.
* **교집합 (Intersection / And)**: 사건 $A$와 $B$가 동시에 발생할 확률 (쉼표 `,` 또는 병렬 표기 $AB$로 아주 많이 축약함)
  $$P(A \cap B) = P(A \text{ and } B) = P(A, B) = P(AB)$$
* **합집합 (Union / Or)**: 사건 $A$ 또는 $B$가 발생할 확률
  $$P(A \cup B) = P(A \text{ or } B)$$
* **차집합 (Difference)**: 사건 $A$에서 $B$를 제외한 사건의 확률
  $$P(A \setminus B) = P(A - B) = P(A \cap B^c)$$
* **여집합 (Complement / Not)**: 사건 $A$가 발생하지 않을 확률
  $$P(A^c) = P(A') = P(\bar{A})$$

---


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

## 4. Example: Presidential Election Probability

**[Problem]**
In a presidential election, there are four candidates: A, B, C, and D. Based on our polling analysis, we estimate that A has a 20 percent chance of winning the election, while B has a 40 percent chance of winning. What is the probability that A or B wins the election?

---

**[Solution & Explanation]**

### 1. Definition of Sample Space ($S$) and Outcomes
Let the elementary outcomes (elements) representing the winner of the election be $a, b, c,$ and $d$:
* $a$: The outcome that candidate A wins.
* $b$: The outcome that candidate B wins.
* $c$: The outcome that candidate C wins.
* $d$: The outcome that candidate D wins.

The sample space $S$ is the set of all possible outcomes:
$$S = \{a, b, c, d\}$$

### 2. Definition of Events
An event is a subset of the sample space $S$. Using set-builder notation and roster method:
* **Event $E_A$ (A wins)**: 
  $$E_A = \{ x \in S \mid x \text{ is the outcome that candidate A wins} \} = \{a\}$$
* **Event $E_B$ (B wins)**: 
  $$E_B = \{ x \in S \mid x \text{ is the outcome that candidate B wins} \} = \{b\}$$

### 3. Mutually Exclusive (Disjoint) Events
Since there can be only one winner in the election, the outcomes $a$ and $b$ cannot occur simultaneously.
Thus, the intersection of events $E_A$ and $E_B$ is the empty set:
$$E_A \cap E_B = \{a\} \cap \{b\} = \emptyset \quad \text{(Disjoint Events)}$$

### 4. Probability Calculation (Applying Axiom 3)
We want to find the probability that A or B wins, which corresponds to the union $E_A \cup E_B$.
We are given:
* $P(E_A) = 0.20$
* $P(E_B) = 0.40$

Since $E_A$ and $E_B$ are disjoint, by **Kolmogorov's Axiom 3 (Countable Additivity)**:
$$P(E_A \cup E_B) = P(E_A) + P(E_B)$$
$$P(E_A \cup E_B) = 0.20 + 0.40 = 0.60 \quad (60\%)$$

**[Answer]** The probability that A or B wins the election is **$0.60$ ($60\%$)**.

