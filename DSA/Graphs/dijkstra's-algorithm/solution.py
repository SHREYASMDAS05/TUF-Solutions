class Solution:
    def dijkstra(self, V, edges, S):
        dist = [10**9] * V
        dist[S] = 0
        heap = [(0,S)] #as it need to be sorted based onthe distnance to get the lest distmce at top 
        adj = [[] for i in range(V)]
        for u , v , w in edges:
            adj[v].append((u,w))
            adj[u].append((v ,w))
        while heap:
            current_dist , u = heapq.heappop(heap)
            

            for v , w in adj[u]:
                new_dist = current_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap , (new_dist , v))

        return dist

        

    