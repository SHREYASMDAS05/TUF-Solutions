class Solution:
    def canFinish(self, N, arr):
        adj = [[] for i in range(N)]
        indegree = [0] * N 
        for u , v in arr:
            adj[v].append(u)
            indegree[u] += 1
        q = deque()
        for i in range(N):
            if indegree[i] == 0 :
                q.append(i)
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for nei in adj[node]:
                indegree[nei] -=1 
                if indegree[nei] ==0:
                    q.append(nei)

        return N == count
        