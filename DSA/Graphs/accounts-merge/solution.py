from collections import defaultdict


class Unionfind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n

    def find(self, u):
        if u == self.par[u]:
            return u

        self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u, v):
        p_u = self.find(u)
        p_v = self.find(v)

        if p_u == p_v:
            return False

        if self.size[p_u] > self.size[p_v]:
            self.par[p_v] = p_u
            self.size[p_u] += self.size[p_v]
        else:
            self.par[p_u] = p_v
            self.size[p_v] += self.size[p_u]

        return True


class Solution:

    def accountsMerge(self, accounts):

        n = len(accounts)
        uf = Unionfind(n)

        emailtoaccount = {}

        # Connect accounts having common emails
        for i, account in enumerate(accounts):

            for email in account[1:]:

                if email in emailtoaccount:
                    uf.union(i, emailtoaccount[email])
                else:
                    emailtoaccount[email] = i

        # Group emails according to DSU component
        emailgroup = defaultdict(list)

        for email, index in emailtoaccount.items():

            leader = uf.find(index)
            emailgroup[leader].append(email)

        res = []

        # Create final accounts
        for leader, emails in emailgroup.items():

            emails.sort()

            name = accounts[leader][0]

            res.append([name] + emails)

        return res