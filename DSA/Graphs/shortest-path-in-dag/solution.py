class Solution:
    def shortestPath(self, N, M, edges):
        adj = [[] for i in range(N)]
        indegree = [0] * N
        for u , v  , w in edges:
            adj[u].append((v , w))
            indegree[v] += 1

        q = deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
        order = []
        dist = [float('inf')] * N
        dist[0] = 0 
        while q:
            node = q.popleft()
            order.append(node)

            for nei , weight in adj[node]:
                indegree[nei] -=1 
                if indegree[nei] == 0:
                    q.append(nei)
        for node in order:
            for nei , weight in adj[node]:
                dist[nei] = min(dist[nei] ,dist[node] + weight )
        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1
            
        return dist

       