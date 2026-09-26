class Solution:
    def findOrder(self, N, arr):
        adj = [[] for i in range(N)]
        indegree = [0] * N
        for a , b in arr:
            adj[b].append(a)
            indegree[a] += 1
        q = deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)

        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(order) != N:
            return []
        return order

        