# [82. Accounts merge](https://takeuforward.org/practice/dsa/accounts-merge)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given a list of accounts where each element account [i] is a list of strings, where the first element account [i][0]&nbsp;is a name, and the rest of the elements are emails representing emails of the account.

Now, **merge** these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order.

### Example 1:

**Input:** N = 4,

accounts =

[["John","johnsmith@mail.com","john_newyork@mail.com"],

["John","johnsmith@mail.com","john00@mail.com"],

["Mary","mary@mail.com"],

["John","johnnybravo@mail.com"]]

**Output:** [["John","john00@mail.com","john_newyork@mail.com", "johnsmith@mail.com"],

["Mary","mary@mail.com"],

["John","johnnybravo@mail.com"]]

**Explanation:** The first and the second John are the same person as they have a common email. But the third Mary and fourth John are not the same as they do not have any common email.&nbsp;The result can be in any order but the emails must be in sorted order. The following is also a valid result:

[['Mary', 'mary@mail.com'],

['John', 'johnnybravo@mail.com'],

['John', 'john00@mail.com' , 'john_newyork@mail.com', 'johnsmith@mail.com' ]]

### Example 2:

**Input:** N = 6,

accounts =

[["John","j1@com","j2@com","j3@com"],

["John","j4@com"],

["Raj",”r1@com”, “r2@com”],

["John","j1@com","j5@com"],

["Raj",”r2@com”, “r3@com”],

["Mary","m1@com"]]

**Output:** [["John","j1@com","j2@com","j3@com","j5@com"],

["John","j4@com"],

["Raj",”r1@com”, “r2@com”,&nbsp;“r3@com”],

["Mary","m1@com"]]

**Explanation:** The first and the fourth John are the same person here as they have a common email. And the third and the fifth Raj are also the same person. So, the same accounts are merged.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

·&nbsp;&nbsp;1 <= N <= 1000

·&nbsp;&nbsp;2 <= accounts[i].size <= 15

·&nbsp;&nbsp;1 <= accounts[i][j].size <= 30

·&nbsp;&nbsp;accounts[i][0] consists of English letters.

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
