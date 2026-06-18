# 📖 Chapter 1.2: Review of Set Theory — Summary

*Textbook Chapter Link: [Chapter 1.2: Review of Set Theory](https://www.probabilitycourse.com/chapter1/1_2_0_review_set_theory.php)*

이 장은 확률론의 기반이 되는 집합론(Set Theory)의 핵심 개념과 표기법을 다룸. 확률론에서 표본 공간(Sample Space)은 전체집합으로, 사건(Event)은 부분집합으로 다뤄지기 때문에 매우 중요한 단원임. 뒤에서 보겠지만, **확률은 집합에 대해 정의되고 계산됨.**

---

## 1. 집합의 기본 개념 (Basic Definitions)
* **집합 (Set)**: 중복된 어떤 대상(원소, items/elements)이 존재하지 않고, 원소의 순서를 고려하지 않는 Collection임.
* **전체집합 (Universal Set, $S$)**: 논의의 대상이 되는 모든 원소를 포함하는 집합임. 확률론에서는 전체 사건이 발생하는 **표본 공간(Sample Space)**에 해당함.
* **부분집합 (Subset, $A \subset B$)**: 집합 $A$의 모든 원소가 집합 $B$에 속할 때를 의미함.
* **공집합 (Empty Set, $\emptyset$)**: 원소를 아무것도 포함하지 않는 집합임.

### 집합의 수학적 표현 방법
* **원소나열법 (Roster Method)**: 원소를 중괄호 안에 직접 나열하는 방식임. (예: $A = \{1, 2, 3\}$)
* **조건제시법 (Set-builder Notation)**: 원소가 만족해야 하는 수학적 성질을 명시하는 방법임.
    * 표기: $\{x \in S \mid x\text{의 성질}\}$ 또는 $\{x \in S : x\text{의 성질}\}$로 표현함.
    * 기호 `|` 와 `:` 는 **"such that (~를 만족하는)"**을 뜻하며, 둘은 수학적으로 완전히 동일한 의미임.
    * 예시: $\{x \in \mathbb{Z} \mid 1 \le x \le 5\}$ 또는 $\{x \in \mathbb{Z} : 1 \le x \le 5\}$

### 대표적인 숫자 집합 예시
* **$\mathbb{N}$ (자연수)**: $\{1, 2, 3, \dots\}$
* **$\mathbb{Z}$ (정수)**: $\{\dots, -1, 0, 1, \dots\}$
* **$\mathbb{Q}$ (유리수)**: 분수 형태의 수 ($\{\frac{a}{b} \mid a, b \in \mathbb{Z}, b \ne 0\}$)
* **$\mathbb{R}$ (실수)**: 수직선 상의 모든 수 (유리수 + 무리수)
* **$\mathbb{C}$ (복소수)**: 실수부와 허수부로 표현되는 수 ($a + bi$)

### 구간 (Intervals) — 실수의 부분집합
* **닫힌 구간 (Closed Interval)**: 양 끝점을 포함하는 구간임.
    * 표기: $[a, b] = \{x \in \mathbb{R} \mid a \le x \le b\}$
* **열린 구간 (Open Interval)**: 양 끝점을 제외하는 구간임.
    * 표기: $(a, b) = \{x \in \mathbb{R} \mid a < x < b\}$
* **반열린/반닫힌 구간 (Half-open/Half-closed)**: 한쪽 끝점만 포함하는 구간임. (예: $[a, b)$, $(a, b]$)

---

## 2. 벤 다이어그램 (Venn Diagrams)
* 집합 간의 관계(포함 관계, 교집합 등)를 직사각형(전체집합)과 원(사건)을 활용해 시각적으로 나타내는 도구임. 복잡한 사건들의 확률적 연산을 직관적으로 이해할 때 매우 요긴하게 쓰임.

---

## 3. 집합의 연산 (Set Operations)
* **합집합 (Union, $A \cup B$)**: $A$에 속하거나 $B$에 속하는 모든 원소의 집합임.
    $$A \cup B = \{x \in S \mid x \in A \text{ 또는 } x \in B\}$$
* **교집합 (Intersection, $A \cap B$)**: $A$와 $B$에 동시에 속하는 원소들의 집합임.
    $$A \cap B = \{x \in S \mid x \in A \text{ 그리고 } x \in B\}$$
* **여집합 (Complement, $A^c$ or $\bar{A}$)**: 전체집합 $S$에는 속하지만 $A$에는 속하지 않는 원소들의 집합임.
    $$A^c = \{x \in S \mid x \notin A\}$$
* **차집합 (Difference, $A \setminus B$ 또는 $A - B$)**: $A$에는 속하지만 $B$에는 속하지 않는 원소들의 집합임. (대학 수학 레벨에서는 일반적인 사칙연산의 뺄셈 기호 `-`와 혼동을 피하기 위해 백슬래시 기호 `\`를 사용한 $A \setminus B$를 더 널리 사용함)
    $$A \setminus B = A - B = A \cap B^c = \{x \in S \mid x \in A \text{ 그리고 } x \notin B\}$$

* **서로소 집합 (Disjoint Sets)**: 두 집합의 공통 원소가 없을 때를 말함. ($A \cap B = \emptyset$)
* **분할 (Partition)**: 다음 조건을 만족하는 집합군 $A_1, A_2, \dots$를 전체집합 $S$의 분할이라고 함.
    1. 임의의 $i \ne j$에 대해 $A_i \cap A_j = \emptyset$ (서로소임)
    2. $\bigcup_{i} A_i = S$ (합치면 전체집합이 됨)
* **드모르간의 법칙 (De Morgan's Laws)**:
    1. $(A \cup B)^c = A^c \cap B^c$ (합집합의 여집합은 각각의 여집합의 교집합과 같음)
    2. $(A \cap B)^c = A^c \cup B^c$ (교집합의 여집합은 각각의 여집합의 합집합과 같음)
* **분배법칙 (Distributive Laws)**:
    1. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ (교집합에 대한 합집합의 분배임)
    2. $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ (합집합에 대한 교집합의 분배임)

---
## 4. 집합의 크기 (Cardinality)

집합 $A$에 속한 원소의 개수를 기수(Cardinality)라고 하며 $|A|$로 표현함.

* **유한 집합 (Finite Set)**: 원소의 개수가 유한한 집합임. ($|A| < \infty$)
    * **포함-배제의 원리 (Inclusion-Exclusion Principle)**: 유한 집합들의 합집합 크기를 구할 때 사용하는 공식임.
        * 2개 집합: $|A \cup B| = |A| + |B| - |A \cap B|$
        * 3개 집합: $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$
* **무한 집합 (Infinite Set)**: 원소의 개수가 무한한 집합으로 다음과 같이 분류됨:
    * **가산 무한집합 (Countably Infinite Set)**: 자연수 집합($\mathbb{N}$)과 일대일 대응 관계를 만들 수 있는 집합임. 원소를 첫 번째, 두 번째 순서대로 셀 수 있는 무한임.
        * *예: 정수 집합($\mathbb{Z}$), 유리수 집합($\mathbb{Q}$)*
    * **비가산 집합 (Uncountable Set)**: 자연수와 일대일 대응이 불가능하여 원소를 셀 수 없는 무한임.
        * *예: 실수 집합($\mathbb{R}$), 구간 $[0, 1]$의 실수들*

### 곱집합 (Cartesian Product)과 곱의 법칙 (Multiplication Principle)

집합의 크기를 계산하고 확장할 때 기반이 되는 핵심 개념임.

* **곱집합 (Cartesian Product, $A \times B$)**:
    * 두 집합 $A$와 $B$의 원소들로 만들 수 있는 모든 순서쌍(Ordered Pairs)의 집합임.
    * 표기: $A \times B = \{(a, b) \mid a \in A, b \in B\}$
    * 크기: 두 유한 집합의 곱집합 크기는 각 집합 크기의 곱과 같음. ($|A \times B| = |A| \times |B|$)
    * **성질 (교환법칙 불성립)**: 순서쌍 내의 순서가 중요하므로, 일반적으로 **교환법칙이 성립하지 않음.**
        ➔ $A \times B \ne B \times A$ (단, $A=B$이거나 공집합인 경우는 제외함)

* **곱의 법칙 (Multiplication Principle)**:
    * 첫 번째 단계를 수행하는 방법이 $m$가지이고, 두 번째 단계를 수행하는 방법이 $n$가지라면, 두 단계를 연이어 수행하는 총 방법은 $m \times n$가지임.
    * 이는 곱집합의 크기 공식($|A \times B| = |A| \times |B|$)을 여러 사건의 선택 과정으로 확장한 것임.
* **확장 (가산성과의 관계)**:
    * $A$와 $B$가 가산 집합(Countable)이면, 그 곱집합 $A \times B$ 역시 가산 집합임. (유리수 집합 $\mathbb{Q}$가 가산 집합임을 증명할 때 이 성질이 쓰임.)

---

## 5. 함수 (Functions)

확률론에서 표본 공간의 원소를 실수값에 대응시키는 확률 변수(Random Variable)를 정의할 때 핵심적으로 사용됨.

* **정의**: 정의역(Domain, $A$)의 각 원소를 공역(Codomain, $B$)의 **오직 하나의 원소**에 대응시키는 규칙임. 수학적으로 온전한 함수를 정의하기 위해서는 **타입 선언**과 **대응 규칙**이 모두 필요함.
    * **타입 선언 (Signature / Type Declaration)**: $f: A \rightarrow B$
        * 함수가 작동할 범위(정의역 $A$)와 결과가 담길 범위(공역 $B$)를 명시함.
        * 여기서 콜론 `:`은 영어로 **"is a function from (~에서 ~로 가는 함수)"**를 뜻함. 즉, **"$f$ is a function from $A$ to $B$"** ($f$는 $A$에서 $B$로 가는 함수)로 읽음.
    * **대응 규칙 (Mapping Rule / Formula)**: $f(x) = x + 1$
        * 입력값 $x$가 들어왔을 때 출력값 $f(x)$가 계산되는 구체적인 수학적 연산 식을 나타냄.
    * **필요성**: 실제 대응 규칙이 같더라도, 정의역과 공역이 다르면 수학적으로 완전히 다른 함수임.
        * **함수 1**: $f_1 : \mathbb{Z} \rightarrow \mathbb{Z}$ 이고 $f_1(x) = x^2$
            * 정의역이 정수이므로 $x = 1.5$는 대입할 수 없음.
        * **함수 2**: $f_2 : \mathbb{R} \rightarrow \mathbb{R}$ 이고 $f_2(x) = x^2$
            * 정의역이 실수이므로 $x = 1.5$를 대입할 수 있고 ($2.25$가 됨), 연속함수(Continuous function)가 됨.
        * 이처럼 입력과 출력의 범위를 명확히 명시하기 위해 타입 선언과 대응 규칙 두 선언이 모두 필수적임.
* **치역 (Range)**: 정의역의 모든 원소 $x$에 대해 함수가 실제로 갖는 모든 함숫값 $f(x)$들의 집합임. 치역은 항상 공역의 부분집합임. ($Range(f) \subset B$)

---

## 6. Detailed Solution for Example 1.5

**[Problem]**
In a party,

* There are $10$ people wearing white shirts and $8$ people wearing red shirts.
* $4$ people have black shoes and white shirts.
* $3$ people have black shoes and red shirts.
* The total number of people wearing white or red shirts or black shoes is $21$.
* Find the number of people wearing black shoes.

---

**[Solution & Explanation]**

### 1. Definition of Universal Set ($S$) and Outcomes
Let the universal set $S$ be the set of all people attending the party:
$$S = \{ x \mid x \text{ is a person at the party} \}$$

### 2. Definition of Subsets
Define the subsets of interest using set-builder notation:

* $W$: The set of people wearing white shirts.
    $$W = \{ x \in S \mid x \text{ is wearing a white shirt} \}$$
* $R$: The set of people wearing red shirts.
    $$R = \{ x \in S \mid x \text{ is wearing a red shirt} \}$$
* $B$: The set of people wearing black shoes.
    $$B = \{ x \in S \mid x \text{ is wearing black shoes} \}$$

We are given the following cardinalities:

* $|W| = 10$
* $|R| = 8$
* $|W \cap B| = 4$
* $|R \cap B| = 3$
* $|W \cup R \cup B| = 21$

### 3. Relationships between Sets
* It is reasonable to assume that a person cannot wear both a white shirt and a red shirt at the same time. Therefore, the sets $W$ and $R$ are **disjoint** (mutually exclusive):
    $$W \cap R = \emptyset \implies |W \cap R| = 0$$
* Since $W$ and $R$ are disjoint, no person can wear a white shirt, a red shirt, and black shoes simultaneously:
    $$W \cap R \cap B = \emptyset \implies |W \cap R \cap B| = 0$$

### 4. Calculation (Applying the Inclusion-Exclusion Principle)
Using the Inclusion-Exclusion Principle for three finite sets:
$$|W \cup R \cup B| = |W| + |R| + |B| - |W \cap R| - |W \cap B| - |R \cap B| + |W \cap R \cap B|$$

Substitute the known values into the equation:
$$21 = 10 + 8 + |B| - 0 - 4 - 3 + 0$$
$$21 = 11 + |B|$$
$$|B| = 10$$

**[Answer]** The number of people wearing black shoes is **$10$**.

