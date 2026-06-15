# 📖 Chapter 1.2: Review of Set Theory — Summary

*Textbook Chapter Link: [Chapter 1.2: Review of Set Theory](https://www.probabilitycourse.com/chapter1/1_2_0_review_set_theory.php)*

이 장은 확률론의 기반이 되는 집합론(Set Theory)의 핵심 개념과 표기법을 다룹니다. 확률론에서 표본 공간(Sample Space)은 전체집합으로, 사건(Event)은 부분집합으로 다뤄지기 때문에 매우 중요한 단원입니다. 뒤에서 보겠지만, **확률은 집합에 대해 정의되고 계산됩니다**

---

## 1. 집합의 기본 개념 (Basic Definitions)

* **집합 (Set)**: 중복된 어떤 대상(원소, items/elements)이 존재하지 않고, 원소의 순서를 고려하지 않는 Collection입니다.
* **전체집합 (Universal Set, $S$)**: 논의의 대상이 되는 모든 원소를 포함하는 집합입니다. 확률론에서는 전체 사건이 발생하는 **표본 공간(Sample Space)**에 해당합니다.
* **부분집합 (Subset, $A \subset B$)**: 집합 $A$의 모든 원소가 집합 $B$에 속할 때를 의미합니다.
* **공집합 (Empty Set, $\emptyset$)**: 원소를 아무것도 포함하지 않는 집합입니다.

### 집합의 수학적 표현 방법
* **원소나열법 (Roster Method)**: 원소를 중괄호 안에 직접 나열하는 방식입니다. (예: $A = \{1, 2, 3\}$)
* **조건제시법 (Set-builder Notation)**: 원소가 만족해야 하는 수학적 성질을 명시하는 방법입니다.
  * 표기: $\{x \in S \mid x\text{의 성질}\}$ (예: $\{x \in \mathbb{Z} \mid 1 \le x \le 5\}$)

### 대표적인 숫자 집합 예시
* **$\mathbb{N}$ (자연수)**: $\{1, 2, 3, \dots\}$
* **$\mathbb{Z}$ (정수)**: $\{\dots, -1, 0, 1, \dots\}$
* **$\mathbb{Q}$ (유리수)**: 분수 형태의 수 ($\{\frac{a}{b} \mid a, b \in \mathbb{Z}, b \ne 0\}$)
* **$\mathbb{R}$ (실수)**: 수직선 상의 모든 수 (유리수 + 무리수)
* **$\mathbb{C}$ (복소수)**: 실수부와 허수부로 표현되는 수 ($a + bi$)

### 구간 (Intervals) — 실수의 부분집합
* **닫힌 구간 (Closed Interval)**: 양 끝점을 포함하는 구간
  * 표기: $[a, b] = \{x \in \mathbb{R} \mid a \le x \le b\}$
* **열린 구간 (Open Interval)**: 양 끝점을 제외하는 구간
  * 표기: $(a, b) = \{x \in \mathbb{R} \mid a < x < b\}$
* **반열린/반닫힌 구간 (Half-open/Half-closed)**: 한쪽 끝점만 포함하는 구간 (예: $[a, b)$, $(a, b]$)

---

## 2. 벤 다이어그램 (Venn Diagrams)
* 집합 간의 관계(포함 관계, 교집합 등)를 직사각형(전체집합)과 원(사건)을 활용해 시각적으로 나타내는 도구입니다. 복잡한 사건들의 확률적 연산을 직관적으로 이해할 때 매우 요긴하게 쓰입니다.

---

## 3. 집합의 연산 (Set Operations)
* **합집합 (Union, $A \cup B$)**: $A$에 속하거나 $B$에 속하는 모든 원소의 집합입니다.
  $$A \cup B = \{x \in S \mid x \in A \text{ 또는 } x \in B\}$$
* **교집합 (Intersection, $A \cap B$)**: $A$와 $B$에 동시에 속하는 원소들의 집합입니다.
  $$A \cap B = \{x \in S \mid x \in A \text{ 그리고 } x \in B\}$$
* **여집합 (Complement, $A^c$ or $\bar{A}$)**: 전체집합 $S$에는 속하지만 $A$에는 속하지 않는 원소들의 집합입니다.
  $$A^c = \{x \in S \mid x \notin A\}$$
* **차집합 (Difference, $A - B$)**: $A$에는 속하지만 $B$에는 속하지 않는 원소들의 집합입니다.
  $$A - B = A \cap B^c = \{x \in S \mid x \in A \text{ 그리고 } x \notin B\}$$
* **서로소 집합 (Disjoint Sets)**: 두 집합의 공통 원소가 없을 때를 말합니다. ($A \cap B = \emptyset$)
* **분할 (Partition)**: 다음 조건을 만족하는 집합군 $A_1, A_2, \dots$를 전체집합 $S$의 분할이라고 합니다.
  1. 임의의 $i \ne j$에 대해 $A_i \cap A_j = \emptyset$ (서로소)
  2. $\bigcup_{i} A_i = S$ (합치면 전체집합이 됨)
* **드모르간의 법칙 (De Morgan's Laws)**:
  1. $(A \cup B)^c = A^c \cap B^c$ (합집합의 여집합은 각각의 여집합의 교집합과 같다)
  2. $(A \cap B)^c = A^c \cup B^c$ (교집합의 여집합은 각각의 여집합의 합집합과 같다)

---

## 4. 집합의 크기 (Cardinality)
집합 $A$에 속한 원소의 개수를 기수(Cardinality)라고 하며 $|A|$로 표현합니다.
* **유한 집합 (Finite Set)**: 원소의 개수가 유한한 집합입니다. ($|A| < \infty$)
* **무한 집합 (Infinite Set)**: 원소의 개수가 무한한 집합으로 다음과 같이 분류됩니다:
  * **가산 무한집합 (Countably Infinite Set)**: 자연수 집합($\mathbb{N}$)과 일대일 대응 관계를 만들 수 있는 집합입니다. 원소를 첫 번째, 두 번째 순서대로 셀 수 있는 무한입니다.
    * *예: 정수 집합($\mathbb{Z}$), 유리수 집합($\mathbb{Q}$)*
  * **비가산 집합 (Uncountable Set)**: 자연수와 일대일 대응이 불가능하여 원소를 셀 수 없는 무한입니다.
    * *예: 실수 집합($\mathbb{R}$), 구간 $[0, 1]$의 실수들*

---

## 5. 함수 (Functions)
확률론에서 표본 공간의 원소를 실수값에 대응시키는 확률 변수(Random Variable)를 정의할 때 핵심적으로 사용됩니다.
* **정의**: 정의역(Domain, $A$)의 각 원소를 공역(Codomain, $B$)의 **오직 하나의 원소**에 대응시키는 매핑(Mapping) 규칙입니다. ($f: A \rightarrow B$)
* **치역 (Range)**: 정의역의 모든 원소 $x$에 대해 함수가 실제로 갖는 모든 함숫값 $f(x)$들의 집합입니다. 치역은 항상 공역의 부분집합입니다. ($Range(f) \subset B$)
