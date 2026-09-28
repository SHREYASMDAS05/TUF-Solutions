# [729. Lower Bound](https://takeuforward.org/practice/dsa/lower-bound-)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given a sorted array of nums and an integer x, write a program to find the **lower bound** of **x** .

The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

If no such index is found, return the size of the array.

### Example 1:

**Input:** nums= [1,2,2,3], x = 2

**Output:** 1

**Explanation:**

Index 1 is the smallest index such that arr[1] >= x.

### Example 2:

**Input:** nums= [3,5,8,15,19], x = 9

**Output:** 3

**Explanation:**

Index 3 is the smallest index such that arr[3] >= x.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- &nbsp;&nbsp;1 <= nums.length <= 10^5
- &nbsp;&nbsp;-10^5 < nums[i], x < 10^5
- &nbsp;&nbsp;nums is sorted in ascending order.

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
