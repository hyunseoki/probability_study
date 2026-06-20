# 📖 Chapter 2.1: Combinatorics: Counting Methods — Summary

*Textbook Chapter Link: [Chapter 2.1: Combinatorics](https://www.probabilitycourse.com/chapter2/2_1_0_finding_probabilities_with_counting_methods.php)*

이 장은 경우의 수(Counting)를 활용하여 확률을 계산하는 다양한 조합론적 기법들을 다룸. 표본 공간이 유한하고 각 결과가 발생할 확률이 동일한 등확률 공간(Equally Likely Outcomes)에서 사건의 확률을 구하기 위해 분모와 분자의 경우의 수를 올바르게 세는 능력이 필수적임.

---

## 1. 경우의 수와 확률 (Finding Probabilities with Counting Methods)
* 표본 공간 $S$가 유한하고, 모든 표본 원소(Outcome)가 일어날 가능성이 동일할 때(등확률), 사건 $A$의 확률은 다음과 같이 정의됨.
    $$P(A) = \frac{|A|}{|S|}$$
* 따라서 복잡한 확률 문제를 해결하는 것은 결국 사건 $A$에 해당하는 경우의 수 $|A|$와 전체 표본 공간의 크기 $|S|$를 세는 조합론의 문제로 귀결됨.
* 일반적으로 집합에서 원소를 뽑는 샘플링(Sampling) 문제는 **순서(Order)의 고려 여부**와 **중복(Replacement) 허용 여부**에 따라 아래의 4가지 기본 기법으로 분류됨.

---

## 2. 샘플링 기법의 4가지 분류 (The Four Basic Sampling Methods)

집합 $\{1, 2, \dots, n\}$에서 $k$개의 원소를 뽑는 상황을 가정함.

| 분류 | 중복 허용 (With Replacement) | 중복 불허 (Without Replacement) |
| :--- | :--- | :--- |
| **순서 있음 (Ordered)** | **중복순열** (Ordered with replacement)<br>공식: $n^k$ | **순열** (Permutation / Ordered without replacement)<br>공식: $P^n_k = \frac{n!}{(n-k)!}$ |
| **순서 없음 (Unordered)** | **중복조합** (Unordered with replacement)<br>공식: $\binom{n+k-1}{k}$ | **조합** (Combination / Unordered without replacement)<br>공식: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ |

---

## 3. 세부 기법 설명 (Detailed Methods)

### (1) 순서 있고 중복 허용 (Ordered with Replacement) — 중복순열
* **정의**: $n$개의 서로 다른 대상 중에서 한 개를 뽑고 다시 돌려놓는 시행을 $k$번 반복하며, 뽑힌 순서를 고려하는 경우임.
* **공식**: 첫 번째부터 $k$번째 선택까지 매번 $n$가지의 선택지가 존재하므로 곱의 법칙에 의해 다음 공식을 얻음.
    $$N = n \times n \times \dots \times n = n^k$$
* *예시*: 4자리 숫자로 된 자물쇠의 비밀번호 설정 개수 ($10^4 = 10,000$가지).

### (2) 순서 있고 중복 없음 (Ordered without Replacement) — 순열 (Permutation)
* **정의**: $n$개의 서로 다른 대상 중에서 하나를 뽑아 나열하되, 한 번 뽑은 원소는 다시 뽑지 않고 순서를 고려하는 경우임.
* **공식**: 첫 선택지는 $n$개, 두 번째는 $n-1$개, $\dots$, $k$번째는 $n-k+1$개이므로 곱의 법칙에 의해 다음과 같음.
    $$P^n_k = n(n-1)(n-2)\cdots(n-k+1) = \frac{n!}{(n-k)!}$$
    *(단, $k > n$이면 $P^n_k = 0$이며, $n! = n(n-1)\cdots 1$이고 $0! = 1$로 정의함)*
* *예시*: 10명의 육상 선수 중 금, 은, 동메달을 목에 걸 선수를 순서대로 뽑는 경우 ($P^{10}_3 = 10 \times 9 \times 8 = 720$가지).

### (3) 순서 없고 중복 없음 (Unordered without Replacement) — 조합 (Combination)
* **정의**: $n$개의 서로 다른 대상 중에서 순서에 상관없이 중복을 허용하지 않고 $k$개의 원소를 그룹으로 선택하는 경우임.
* **공식**: 순열 $P^n_k$에서 순서에 의해 중복 계산된 $k!$만큼 나누어 줌으로써 정의됨. 이를 이항계수(Binomial Coefficient)라고 부름.
    $$\binom{n}{k} = C^n_k = \frac{P^n_k}{k!} = \frac{n!}{k!(n-k)!}$$
* **성질**:
    1. 대칭성: $\binom{n}{k} = \binom{n}{n-k}$ (즉, $k$개를 선택하는 것은 남겨둘 $n-k$개를 선택하는 것과 동일함)
    2. 경계값: $\binom{n}{0} = \binom{n}{n} = 1$
* **이항 정리 (Binomial Theorem)**:
    $$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$$

### (4) 순서 없고 중복 허용 (Unordered with Replacement) — 중복조합
* **정의**: $n$개의 서로 다른 범주에서 중복을 허용하여 순서 없이 총 $k$개의 원소를 선택하는 경우임.
* **공식**: 공과 칸막이 모델(Stars and Bars)을 통해 유도됨.
    $$\binom{n+k-1}{k} = \binom{n+k-1}{n-1}$$
* **공과 칸막이 모델 (Stars and Bars)**:
    * $k$개의 똑같은 공(★)과 서로 다른 $n$개의 영역을 구분하기 위한 $(n-1)$개의 칸막이(|)를 일렬로 나열하는 경우의 수와 같음.
    * 총 자릿수 $(k + n - 1)$개 중 공이 들어갈 $k$개의 자리를 선택하는 것과 같으므로 $\binom{n+k-1}{k}$가 됨.
* **정수해 방정식과의 관계**:
    * 방정식 $x_1 + x_2 + \dots + x_n = k$의 해의 개수 구하기:
        1. **음이 아닌 정수해** ($x_i \ge 0$): 위 공식과 동일하게 $\binom{n+k-1}{k}$가지임.
        2. **양의 정수해** ($x_i \ge 1$): 미리 각 변수에 $1$씩을 미리 나누어 준 뒤 남은 $(k-n)$개의 공을 $n$개의 상자에 배분하는 것과 같으므로, $\binom{n+(k-n)-1}{k-n} = \binom{k-1}{n-1}$가지가 됨.

---

## 4. Detailed Solutions for Chapter 2 Examples

### **Example 2.1**
**[Problem]**
A basket contains $5$ red balls and $7$ white balls. We draw $3$ balls from the basket. Find the probability that all $3$ balls are red under the following two conditions:
1. The drawing is done with replacement.
2. The drawing is done without replacement.

---

**[Solution]**

#### 1. With Replacement (복원추출)
매번 뽑을 때마다 주머니의 상황이 동일함. 전체 공의 개수는 $5 + 7 = 12$개임.
* **표본 공간 크기 $|S|$**: 순서대로 복원추출하므로 $12^3 = 1728$임.
* **사건 $A$ (모두 빨간 공) 크기 $|A|$**: 매번 빨간 공 $5$개 중 하나를 고르므로 $5^3 = 125$임.
* **확률**:
    $$P(A) = \frac{5^3}{12^3} = \left(\frac{5}{12}\right)^3 = \frac{125}{1728} \approx 0.0723$$

#### 2. Without Replacement (비복원추출)
순서를 고려하지 않고 $12$개 중 $3$개를 고르는 조합으로 생각할 수 있음.
* **표본 공간 크기 $|S|$**: $\binom{12}{3} = \frac{12 \times 11 \times 10}{3 \times 2 \times 1} = 220$임.
* **사건 $A$ (모두 빨간 공) 크기 $|A|$**: 빨간 공 $5$개 중 $3$개를 순서 없이 고르므로 $\binom{5}{3} = \binom{5}{2} = 10$임.
* **확률**:
    $$P(A) = \frac{\binom{5}{3}}{\binom{12}{3}} = \frac{10}{220} = \frac{1}{22} \approx 0.0455$$

---

### **Example 2.2**
**[Problem]**
Find the number of non-negative integer solutions to the equation:
$$x_1 + x_2 + x_3 + x_4 = 12$$
Also find the number of positive integer solutions.

---

**[Solution]**

#### 1. Non-negative Integer Solutions (음이 아닌 정수해: $x_i \ge 0$)
이 문제는 $4$개의 서로 다른 변수($n=4$)에 $12$개의 단위 값($k=12$)을 나누어 주는 중복조합의 수와 같음.
* **공식 적용**: $\binom{n+k-1}{k} = \binom{4+12-1}{12} = \binom{15}{12}$
* **계산**:
    $$\binom{15}{12} = \binom{15}{3} = \frac{15 \times 14 \times 13}{3 \times 2 \times 1} = 455$$
* **정답**: 음이 아닌 정수해의 개수는 **$455$개**임.

#### 2. Positive Integer Solutions (양의 정수해: $x_i \ge 1$)
각 변수가 적어도 $1$ 이상이어야 하므로, 변환 $y_i = x_i - 1 \ge 0$을 사용함.
이를 원 방정식에 대입하면:
$$(y_1 + 1) + (y_2 + 1) + (y_3 + 1) + (y_4 + 1) = 12 \implies y_1 + y_2 + y_3 + y_4 = 8$$
여기서 $y_i \ge 0$인 음이 아닌 정수해의 개수를 구하는 중복조합 문제로 단순화됨 ($n=4, k'=8$).
* **공식 적용**: $\binom{k-1}{n-1} = \binom{12-1}{4-1} = \binom{11}{3}$
* **계산**:
    $$\binom{11}{3} = \frac{11 \times 10 \times 9}{3 \times 2 \times 1} = 165$$
* **정답**: 양의 정수해의 개수는 **$165$개**임.
