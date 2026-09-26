# [425. Find eventual safe states](https://takeuforward.org/practice/dsa/find-eventual-safe-states)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given a directed graph with V vertices labeled from 0 to V-1. The graph is represented using an adjacency list where adj[i] lists all nodes adjacent to node i, meaning there is an edge from node i to each node in adj[i]. A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node. Return an array containing all the **safe nodes** of the graph in **ascending** order.

### Example 1:

**Input:** &nbsp;V = 7, adj= [[1,2], [2,3], [5], [0], [5], [], []]

<img src="https://static.takeuforward.org/content/1788144840_cofLYUqO.webp">

**Output:** [2, 4, 5, 6]

**Explanation:** &nbsp;

From node 0: two paths are there 0->2->5 and 0->1->3->0.&nbsp;

The second path does not end at a terminal node. So it is not&nbsp;

a safe node.

From node 1: two paths exist: 1->3->0->1 and 1->2->5.

But the first one does not end at a terminal node. So it is not a safe node.

From node 2: only one path: 2->5 and 5 is a terminal node.

So it is a safe node.

From node 3: two paths: 3->0->1->3 and 3->0->2->5&nbsp;

but the first path does not end at a terminal node.&nbsp;

So it is not a safe node.

From node 4: Only one path: 4->5 and 5 is a terminal node.&nbsp;

So it is also a safe node.

From node 5: It is a terminal node.&nbsp;

So it is a safe node as well.

From node 6: It is a terminal node.&nbsp;

So it is a safe node as well.

### Example 2:

**Input:** &nbsp;V = 4, adj= [[1], [2], [0,3], []]

<img src="https://static.takeuforward.org/content/1788144877_35G_KkO9.webp">

**Output:** [3]

**Explanation:** Node 3 itself is a terminal node and it&nbsp;is a safe node as well. But all the paths&nbsp;from other nodes do not lead to a terminal node.So they are&nbsp;excluded from the answer.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- &nbsp;&nbsp;V == adj.length
- &nbsp;&nbsp;1 <= V <= 10^4
- &nbsp;&nbsp;0 <= adj[i].length <= n
- &nbsp;&nbsp;0 <= adj[i][j] <= n - 1
- &nbsp;&nbsp;adj[i] is sorted in a strictly increasing order.
- &nbsp;&nbsp;The graph may contain self-loops.
- &nbsp;&nbsp;The number of edges in the graph will be in the range [1, 4 * 10^4].

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
