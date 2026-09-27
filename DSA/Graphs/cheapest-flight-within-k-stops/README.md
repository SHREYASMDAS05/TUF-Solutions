# [71. Cheapest flight within K stops](https://takeuforward.org/practice/dsa/cheapest-flight-within-k-stops)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

There are n cities and m edges connected by some number of flights. Given an array of flights where flights[i] = [ from_i, to_i, price_i] indicates that there is a flight from city from_i to city to_i with cost price_i. Given three integers src, dst, and k, and return the **cheapest price** from src to dst with at most **k** stops. If there is no such route, return -1.

### Example 1:

<img src="https://static.takeuforward.org/content/1789073726_xU-q_k_l.webp">

**Input:** n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1

**Output:** 700

**Explanation:** The optimal path with at most 1 stops from city 0 to 3 is marked in red and has cost 100 + 600 = 700.

Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

### Example 2:

<img src="https://static.takeuforward.org/content/1789479845_h5m1peyr.webp">

**Input:** n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1

**Output:** 200

**Explanation:** The optimal path with at most 1 stops from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- &nbsp;&nbsp;1 <= n <= 100
- &nbsp;&nbsp;0 <= flights.length <= (n * (n - 1) / 2)
- &nbsp;&nbsp;&nbsp;flights[i].length == 3
- &nbsp;&nbsp;0 <= from_i, to_i < n
- &nbsp;&nbsp;from_i != to_i
- &nbsp;&nbsp;1 <= price_i <= 10^4
- &nbsp;&nbsp;There will not be any multiple flights between the two cities.
- &nbsp;&nbsp;0 <= src, dst, k < n

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
