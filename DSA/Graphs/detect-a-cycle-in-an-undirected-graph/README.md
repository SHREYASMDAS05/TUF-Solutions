# [190. Detect a cycle in an undirected graph](https://takeuforward.org/practice/dsa/detect-a-cycle-in-an-undirected-graph)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given an undirected graph with V vertices labeled from 0 to V-1.&nbsp;The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Determine if the graph contains any **cycles** .

**Note:** The graph does not contain any self-edges (edges where a vertex is connected to itself).

### Example 1:

<img src="https://static.takeuforward.org/content/ProblemSetter-Eymk2V2R">

**Input:** &nbsp;V = 6, adj= [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

**Output:** True

**Explanation:** The graph contains a cycle: 0 ->1 -> 2 -> 5 -> 4 -> 1.

### Example 2:

<img src="https://static.takeuforward.org/content/ProblemSetter-ddy9fw2d">

**Input:** &nbsp;V = 4, adj= [[1, 2], [0], [0, 3], [2]]

**Output:** False

**Explanation:** The graph does not contain any cycles.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- E=number of edges
- 1 ≤ V, E ≤ 10<sup style="color:var(--text-color);background-color:var(--background)">4</sup>

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
