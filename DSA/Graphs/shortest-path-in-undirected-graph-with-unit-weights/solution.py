class Solution:
    def shortestPath(self, edges, N, M):
        adj = [[] for i in range(N)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        q = deque()
        q.append(0)
        visit.add(0)
        dist = [-1] * N
        dist[0] = 0 
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in visit:
                    dist[nei] = 1 + dist[node]
                    q.append(nei)
                    visit.add(nei)
        return dist

      