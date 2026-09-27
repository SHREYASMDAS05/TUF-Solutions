import heapq
class Solution:
    def shortestPath(self,n, m, edges):
        adj = [[] for i in range(n+1)]
        for u , v , w in edges:
            adj[u].append((v , w))
            adj[v].append((u,w))
        heap = [(0,1)]
        distance = [float('inf')] * (n+1)
        distance[1] = 0
        parent = [-1] * (n+1)
        while heap:
            curr_dist , node = heapq.heappop(heap)

            if curr_dist > distance[node]:
                continue
            for v , weight in adj[node]:
                new_dist = curr_dist + weight

                if new_dist < distance[v]:
                    distance[v]  = new_dist
                    parent[v] = node 
                    heapq.heappush(heap , (new_dist , v))

        if distance[n] == float('inf'):
            return [-1]
        path = []
        current = n
        while current != -1:
            path.append(current)
            current = parent[current]
        path.append(distance[n])
        path.reverse()
        return path


