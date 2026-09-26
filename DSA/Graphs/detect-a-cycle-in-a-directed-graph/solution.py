from collections import deque 
class Solution:
    def isCyclic(self, N, adj):
        indegree = [0] * N
        for u in range(N):
            for v in adj[u]:
                indegree[v] += 1
        q = deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -=1

                if indegree[nei] == 0:
                    q.append(nei)

        return len(res) != N


        