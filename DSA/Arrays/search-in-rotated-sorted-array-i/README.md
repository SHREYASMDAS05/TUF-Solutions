# [46. Search in rotated sorted array-I](https://takeuforward.org/practice/dsa/search-in-rotated-sorted-array-i)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is **rotated** at some pivot point that is unknown. Find the **index** at which k is present and if k is not present return -1.

### Example 1:

Input : nums = [4, 5, 6, 7, 0, 1, 2], k = 0

Output: 4

Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

### Example 2:

Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3

Output: -1

Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- &nbsp;&nbsp;1 <= nums.length <= 10^4
- &nbsp;&nbsp;-10^4 <= nums[i] <= 10^4
- &nbsp;&nbsp;All values of nums are unique.
- &nbsp;&nbsp;nums is an ascending array that is possibly rotated.
- &nbsp;&nbsp;-10^4 <= k <= 10^4

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
