# [857. Minimum multiplications to reach end](https://takeuforward.org/practice/dsa/minimum-multiplications-to-reach-end)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given start, end, and an array arr of n numbers. At each step, the start is multiplied by any number in the array and then a mod operation with 100000 is done to get the new start.

Find the **minimum steps** in which the end can be achieved starting from the start. If it is not possible to reach the end, then return -1.

### Example 1:

**Input:** arr = [2, 5, 7], start = 3, end = 30

**Output:** 2

**Explanation:**

Step 1: 3*2 = 6 % 100000 = 6&nbsp;

Step 2: 6*5 = 30 % 100000 = 30

Therefore, in minimum 2 multiplications, we reach the&nbsp;end number which is treated as a destination&nbsp;node of a graph here.

### Example 2:

**Input:** arr = [3, 4, 65], start = 7, end = 66175

**Output:** 4

**Explanation:**

Step 1: 7*3 = 21 % 100000 = 21&nbsp;

Step 2: 21*3 = 63 % 100000 = 63&nbsp;

Step 3: 63*65 = 4095 % 100000 = 4095&nbsp;

Step 4: 4095*65 = 266175 % 100000 = 66175

Therefore, in minimum 4 multiplications we reach the end number which is treated as a destination node of a graph here.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- &nbsp;&nbsp;1 <= n <= 10^4
- &nbsp;&nbsp;1 <= arr[i] <= 10^4
- &nbsp;&nbsp;1 <= start, end < 10^5

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
