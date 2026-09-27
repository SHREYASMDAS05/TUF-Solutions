class DisjointSet:

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    # Returns the representative of the set containing u
    def findParent(self, u):
        if u == self.parent[u]:
            return u

        # Path compression
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]

    # Checks whether u and v belong to the same set
    def find(self, u: int, v: int) -> bool:
        return self.findParent(u) == self.findParent(v)

    # Union using rank
    def unionByRank(self, u: int, v: int) -> None:

        pu = self.findParent(u)
        pv = self.findParent(v)

        # Already in the same set
        if pu == pv:
            return

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

    # Union using size
    def unionBySize(self, u: int, v: int) -> None:

        pu = self.findParent(u)
        pv = self.findParent(v)

        # Already in the same set
        if pu == pv:
            return

        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]

        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]