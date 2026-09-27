import heapq
class Solution:
    def swimInWater(self, grid):
        # Your code goes here
        heap = [(grid[0][0] , 0 , 0 )]
        directions = [(0,1) , (0,-1) , (-1,0) , (1,0)]
        row , col = len(grid) , len(grid[0])
        visited = set()
        visited.add((0,0))
        while heap:
            time , r , c = heapq.heappop(heap)

            if r == row - 1 and c == col -1 :
                return time 
            for dr , dc in directions:
                nr , nc = r + dr , c + dc 
                if 0<= nr < row and 0 <= nc < col and (nr,nc) not in visited:
                    new_time = max(time , grid[nr][nc])
                    heapq.heappush(heap,(new_time , nr , nc))
                    visited.add((nr,nc))

        
