# [810. Disjoint Set](https://takeuforward.org/practice/dsa/disjoint-set-)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Design a disjoint set (also called union-find) data structure that supports the following operations:

DisjointSet(int n) initializes the disjoint set with n elements.

void unionByRank(int u, int v) merges the sets containing u and v using the rank heuristic.

void unionBySize(int u, int v) merges the sets containing u and v using the size heuristic.

bool find(int u, int v) checks if the elements u and v are in the same set and returns true if they are, otherwise false.

### Example 1:

Input:

["DisjointSet", "unionByRank", "unionBySize", "find", "find"]

[[5], [0, 1], [2, 3], [0, 1], [0, 3]]

Output:

[null, null, null, true, false]

Explanation:

DisjointSet ds = new DisjointSet(5); // Initialize a disjoint set with 5 elements

ds.unionByRank(0, 1); // Merge sets containing 0 and 1 using rank

ds.unionBySize(2, 3); // Merge sets containing 2 and 3 using size

ds.find(0, 1); // Returns true as 0 and 1 are in the same set

ds.find(0, 3); // Returns false as 0 and 3 are not in the same set

### Example 2:

Input:

["DisjointSet", "unionBySize", "unionBySize", "find", "find"]

[[3], [0, 1], [1, 2], [0, 2], [0, 1]]

Output:

[null, null, null, true, true]

Explanation:

DisjointSet ds = new DisjointSet(3); // Initialize a disjoint set with 3 elements

ds.unionBySize(0, 1); // Merge sets containing 0 and 1 using size

ds.unionBySize(1, 2); // Merge sets containing 1 and 2 using rank

ds.find(0, 2); // Returns true as 0 and 2 are in the same set

ds.find(0, 1); // Returns true as 0 and 1 are in the same set

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- 1 <= n <= 10^4
- 0 <= u, v < n
- At most 5 * 10^4 calls will be made to unionByRank, unionBySize, and find

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
