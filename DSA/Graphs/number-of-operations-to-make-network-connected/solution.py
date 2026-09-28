class Unionfind:
    def __init__(self , n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.rank = [0] * n
    def find(self , u):
        if u == self.par[u]:
            return u 
        self.par[u] = self.find(self.par[u])
        return self.par[u]
    def union(self , u , v):
        p_u = self.find(u)
        p_v = self.find(v)

        if p_u == p_v :
            return False
        if self.size[p_u] > self.size[p_v]:
            self.par[p_v] = p_u
            self.size[p_u] += self.size[p_v]
        else:
            self.par[p_u] = p_v
            self.size[p_v] += self.size[p_u]
        return True

class Solution:
    def solve(self, n, Edge):
        uf = Unionfind(n)
        if len(Edge) < n-1 :
            return -1 
        components = n
        for u , v in Edge:
            if uf.union(u,v):
                components -= 1
        return components - 1 

       