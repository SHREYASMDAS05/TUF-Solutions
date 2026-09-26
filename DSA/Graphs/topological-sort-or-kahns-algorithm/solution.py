class Solution:
    def topoSort(self, V, adj):
        indegree  = [0] * V
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1

        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0 :
                    q.append(nei)

        return res
    


       
