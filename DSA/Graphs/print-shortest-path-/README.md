# [969. Print Shortest Path](https://takeuforward.org/practice/dsa/print-shortest-path-)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given a **weighted** undirected graph having n vertices numbered from 1 to n and m edges describing there are edges, where edges[i]=[a_i,b_i,w_i], representing an edge from vertex a_i to b_i with weight w_i.

Find the **shortest path** between the vertex 1 and the vertex n and if path does not exist then return a list consisting of only -1.

If there exists a path, then return a list whose first element is the weight of the path and the remaining elements represent the shortest path from vertex 1 to vertex n.

**Note** : On IDE only the total sum of weights will be shown as output. As there might be more than one path (The path will be validated through driver code and If wrong then output shown will be -2.).

### Example 1:

<img src="https://static.takeuforward.org/content/1789481281_t1ZzErPZ.webp">

**Input:** n = 5, m= 6, edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]

**Output:** 5 1 4 3 5

**Explanation:** &nbsp;The source vertex is 1. Hence, the shortest distance path&nbsp;of node 5 from the source will be 1->4->3->5 as this is&nbsp;the path with a minimum sum of edge weights from source&nbsp;to destination.

### Example 2:

<img src="https://static.takeuforward.org/content/1788096393_02GzAcgU.webp">

**Input:** n = 4, m = 4, edges = [[1,2,2], [2,3,4], [1,4,1],[4,3,3]]

**Output:** 1 1 4&nbsp;

**Explanation:** &nbsp;The source vertex is 1. Hence, the shortest distance&nbsp;path of node 4 from the source will be 1->4 as this is&nbsp;the path with the minimum sum of edge weights from&nbsp;source to destination.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- 2 <= n <= 10^4
- 0 <= m <= 2*10^4
- 1 <= a, b <= n
- 1 <= w <= 10^5

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
