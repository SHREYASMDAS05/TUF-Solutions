# [192. Detect a cycle in a directed graph](https://takeuforward.org/practice/dsa/detect-a-cycle-in-a-directed-graph)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given a **directed** graph with V vertices labeled from 0 to V-1. The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Determine if the graph contains any **cycles** .

### Example 1:

Input:&nbsp;V = 6, adj= [ [1], [2, 5], [3], [4], [1], [ ] ]

<img src="https://static.takeuforward.org/content/ProblemSetter-Do8SOPHS">

Output: True

Explanation: The graph contains a cycle: 1 -> 2 -> 3 -> 4 -> 1.

### Example 2:

Input:&nbsp;V = 4, adj= [[1,2], [2], [], [0,2]]

Output: False

Explanation: The graph does not contain a cycle.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- 1 <= V <= 10^4
- adj.size() == V
- 0 <= adj[i][j] < V
- 1 <= sum(adj[i].size()) <= 10^4

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
