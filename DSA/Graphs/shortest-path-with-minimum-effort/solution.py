class Solution:
    def shortestPath(self, grid, source, destination):
        u , v = destination
        i , j = source 
        rows , cols = len(grid) , len(grid[0])
        if grid[u][v] == 0 or grid[i][j] == 0:
            return -1 
        q = deque()
        q.append((i , j , 0)) # source , distance
        directions = [(0,1) , (0,-1), (1, 0) , (-1,0)]
        visited = set()
        visited.add((i,j))
        while q:
            r , c , dist = q.popleft()
            if [r,c] == destination:
                return dist
            for dr , dc in directions:
                nr , nc = dr + r , dc + c 
                if 0<= nr< rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc] == 1:
                    visited.add((nr,nc))
                    q.append((nr,nc,dist + 1))

        return -1 

        
  
