# [448. Find the city with the smallest number of neighbors](https://takeuforward.org/practice/dsa/find-the-city-with-the-smallest-number-of-neighbors)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [from_i, to_i,weight_i]&nbsp;represents a bidirectional and weighted edge between cities from_i and to_i, and given the integer distance **Threshold** . Find out a city with the **smallest** number of cities that are **reachable** through some path and whose distance is at most Threshold Distance.

If there are multiple such cities, our answer will be the city with the greatest number.

### Example 1:

<img src="https://static.takeuforward.org/content/1789075348_N8Y_LIWN.webp">

Input : N=4, M=4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4

Output: 3

Explanation:&nbsp;

The adjacent cities for each city at a distanceThreshold are =

City 0 →[City 1, City 2]

City 1 →[City 0, City 2, City 3]

City 2 →[City 0, City 1, City 3]

City 3 →[City 1, City 2]

Here, City 0 and City 3 have a minimum number of cities&nbsp;

i.e. 2 within distanceThreshold. So, the result will be the&nbsp;

city with the largest number. So, the answer is City 3.

### Example 2:

<img src="https://static.takeuforward.org/content/1789479909_fSft9MUy.webp">

Input : N=3, M=2, edges = [[0,1,1],[0,2,3]], distanceThreshold = 2

Output: 2

Explanation:&nbsp;

City 0 -> City 1,

City 1 → City 0,

City 2 → no City

Hence, 2 is the answer.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- 1&nbsp;≤&nbsp;n ≤&nbsp;100
- 1 <= m <= n*(n-1)/2
- length(edges[i]) == 3
- 0 <= from_i < to_i < n
- 1 <= weight_i , distanceThreshold <= 10^4
- All pairs (from_i, to_i) are distinct

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
