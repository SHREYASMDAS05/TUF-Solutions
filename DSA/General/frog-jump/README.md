# [321. Frog Jump](https://takeuforward.org/practice/dsa/frog-jump)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

A frog wants to climb a staircase with **n** steps. Given an integer array **heights** , where heights[i] contains the height of the i^th step.

To jump from the **** i^th step to the **** j^th **** step, the frog requires **abs(heights[i] - heights[j])** energy, where abs() denotes the absolute difference. The frog can jump from any step (i^th) either **one** (i+1) or **two** (i+2) **** steps, provided it exists.

Return the **minimum** amount of energy required by the frog to go from the **0** ^ **th** step to the **(n-1)** ^ **th** step.

### Example 1:

**Input:** heights = [2, 1, 3, 5, 4]

**Output:** 2

**Explanation:**

One possible route can be,

0th step -> 2nd Step = abs(2 - 3) = 1

2nd step -> 4th step = abs(3 - 4) = 1

Total = 1 + 1 = 2.

### Example 2:

**Input:** heights = [7, 5, 1, 2, 6]

**Output:** 9

**Explanation:**

One possible route can be,

0th step -> 1st Step = abs(7 - 5) = 2

1st step -> 3rd step = abs(5 - 2) = 3

3rd step -> 4th step = abs(2 - 6) = 4

Total = 2 + 3 + 4 = 9.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- 1 <= n <= 10^4
- 0 <= heights[i] <= 10^4

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
