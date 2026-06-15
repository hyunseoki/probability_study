# 📖 Chapter 1: Basic Concepts — Study Notes

*Textbook Chapter Link: [Chapter 1: Basic Concepts](https://www.probabilitycourse.com/chapter1.php)*

---

## 📌 Core Concepts & Formulas

### 1.1 Introduction to Probability
* **Random Experiment:** An experiment where the outcome cannot be predicted with certainty.
* **Sample Space ($S$):** The set of all possible outcomes.
* **Event ($E$):** Any subset of the sample space.

### 1.2 Sets and Functions
* **Venn Diagrams:** Useful for visualizing relations.
* **Set Operations:**
  * Union: $A \cup B$
  * Intersection: $A \cap B$
  * Complement: $A^c$ or $A'$
* **De Morgan's Laws:**
  1. $(A \cup B)^c = A^c \cap B^c$
  2. $(A \cap B)^c = A^c \cup B^c$

### 1.3 Probability Axioms
For any events in $S$:
1. **Non-negativity:** $P(A) \ge 0$
2. **Normalization:** $P(S) = 1$
3. **Additivity:** If $A_1, A_2, \dots$ are mutually exclusive, then $P(\bigcup_{i=1}^{\infty} A_i) = \sum_{i=1}^{\infty} P(A_i)$

### 1.5 Conditional Probability
* **Definition:** $P(A | B) = \frac{P(A \cap B)}{P(B)}$ (where $P(B) > 0$)

### 1.6 - 1.7 Independent Events
* **Definition:** $A$ and $B$ are independent if and only if $P(A \cap B) = P(A) \cdot P(B)$
* For three events to be independent, they must be pairwise independent AND $P(A \cap B \cap C) = P(A)P(B)P(C)$.

### 1.8 Law of Total Probability
If $B_1, B_2, \dots, B_n$ partition the sample space $S$, then:
$$P(A) = \sum_{i=1}^{n} P(A \cap B_i) = \sum_{i=1}^{n} P(A | B_i) P(B_i)$$

### 1.9 Bayes' Theorem
$$P(B_j | A) = \frac{P(A | B_j) P(B_j)}{\sum_{i=1}^{n} P(A | B_i) P(B_i)}$$

---

## 📐 Solved / Practice Problems Log

*Track key problems from the chapter that you found challenging or interesting.*

### Problem 1.X: [Title]
* **Question:**
  * [Enter question text]
* **Key Idea:**
  * [Method used, e.g., Bayes' Theorem, Law of Total Probability]
* **Solution / Proof:**
  * [Write down the step-by-step derivation]

---

## 💡 Key Takeaways & Summaries
* *Write your general summaries or reflections on Chapter 1 here.*
