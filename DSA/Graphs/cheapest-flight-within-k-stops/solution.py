import heapq
class Solution:
    def CheapestFlight(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj = [[] for i in range(n)]
        for u , v , w in flights:
            adj[u].append((v,w))

        heap = [(0,src,0)] #cost  , node , k 
        while heap:
            cost , node , k = heapq.heappop(heap)
            if node == dst:
                return cost 
            if k == K + 1:
                continue
            for next_city , price in adj[node]:
                new_cost = cost + price 
                heapq.heappush(heap , (new_cost , next_city , k+1))

        return -1


      