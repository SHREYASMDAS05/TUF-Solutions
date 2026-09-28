# [391. Number of operations to make network connected](https://takeuforward.org/practice/dsa/number-of-operations-to-make-network-connected)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given a graph with n vertices and m edges. The graph is represented by an array Edges, where Edge[i] = [a, b] indicates an edge between vertices a and b. One edge can be removed from anywhere and added between any two vertices in one operation. Find the **minimum** number of operations that will be required to make the graph **connected** . If it is not possible to make the graph connected, return -1.

### Example 1:

**Input:** n = 4, Edge =[ [0,&nbsp;1], [ 0, 2], [1, 2]]

<img src="https://static.takeuforward.org/content/1789479267_p0mCzY8-.webp">

**Output:** 1

**Explanation:** We need a minimum of 1 operation to make the two components connected. We can remove the edge (1,2) and add the edge between node 2 and node 3 like the following:

<img src="https://static.takeuforward.org/content/1789479279_-7qC5K1K.webp">

### Example 2:

**Input:** n = 9, Edge = [[0,1],[0,2],[0,3],[1,2],[2,3],[4,5],[5,6],[7,8]]

**Output:** 2

**Explanation:** We need a minimum of 2 operations to make the two components connected. We can remove the edge (0,2) and add the edge between node 3 and node 4 and we can remove the edge (0,3) and add it between nodes 6 and 8 like the following:

<img src="https://static.takeuforward.org/content/1789479296__T8EBjvy.webp">

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- &nbsp;&nbsp;1 <= n <= 10^4
- &nbsp;&nbsp;1 <= Edge.length <= 10^4
- &nbsp;&nbsp;Edge[i].length == 2

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
