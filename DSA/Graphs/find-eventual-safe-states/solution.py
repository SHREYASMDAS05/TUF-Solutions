class Solution:
    def eventualSafeNodes(self, V, adj):


        reverse = [[] for i in range(V)]
        indegree = [0] * V
        for u in range(V):
            for v in adj[u]:
                reverse[v].append(u)
                indegree[u] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        safe = []
        while q:
            node = q.popleft()
            safe.append(node)
            for nei in reverse[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        safe.sort()
        return safe



