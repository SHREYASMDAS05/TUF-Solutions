class Solution:
    def MinimumEffort(self, heights):
        row , col = len(heights) ,len(heights[0])
        min_effort = [[float('inf')] *(col) for i in range(row)]
        heap = [(0 , 0 , 0)]
        min_effort[0][0] = 0
        directions = [(0,1) , (0,-1) , (1,0) , (-1,0)]
        while heap:
            effort , r , c = heapq.heappop(heap)
            if r == row -1 and c == col -1 :
                return effort
            for dr , dc in directions:
                nr , nc = r + dr , c + dc 
                if 0<= nr < row and 0<= nc < col:
                    new_effort = max(effort , abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < min_effort[nr][nc]:
                        min_effort[nr][nc] = min(min_effort[nr][nc] , new_effort)
                        heapq.heappush(heap , (new_effort , nr , nc ))

        return -1 





      