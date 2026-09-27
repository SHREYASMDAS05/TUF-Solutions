# [246. Swim in Rising Water](https://takeuforward.org/practice/dsa/swim-in-rising-water)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

You are given an n × n matrix grid where grid[i][j] is the unique elevation of cell (i, j).

Rain starts falling at time t = 0.

At any later time t ≥ 0, every cell is covered by water to depth t.

You may move 4-directionally (up ⇧, down ⇩, left ⇦, right ⇨) between adjacent cells instantaneously iff the elevations of both cells are ≤ t.

(Think of t as “how high you’re willing to climb”: by time t every elevation ≤ t is underwater and swimmable.)

Starting from the top-left cell (0, 0), return the minimum time t at which you can reach the bottom-right cell (n − 1, n − 1).

### Example 1:

**Input:** grid = [[0,2],[1,3]]

**Output:** 3

**Explanation:**

- t = 0 → only (0,0) is reachable.&nbsp;&nbsp;
- t = 1 → cells {0,0},{1,0} reachable, but (1,1) still blocked (elevation 3).&nbsp;&nbsp;
- t = 2 → cells {0,0},{0,1},{1,0} reachable.&nbsp;&nbsp;
- t = 3 → all cells ≤ 3 are flooded, so we can swim to (1,1).&nbsp;Minimum t = 3.

### Example 2:

**Input:** &nbsp;grid = [[ 0, 1, 2, 3, 4],[24,23,22,21, 5],[12,13,14,15,16],[11,17,18,19,20],[10, 9, 8, 7, 6]]

**Output:** 16

**Explanation:**

- The earliest moment the start and end cells belong to the same flooded component is t = 16.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Example 3:

**Input:** &nbsp;grid = [[0,&nbsp;99,&nbsp;1],[80,&nbsp;2,&nbsp;3],[81, 82,&nbsp;4]]

### Constraints

- n == grid.length
- n == grid[i].length
- 1 ≤ n ≤ 50
- 0 ≤ grid[i][j] < n²
- All elevations are distinct (i.e. grid[i][j] values are unique).

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
