class Solution:
    def ninjaTraining(self, matrix):
        n = len(matrix)
        dp = [[0] * 4 for i in range(n+1) ]
        '''
        def dfs(day , last):
            if day == n:
                return 0 
            points = 0 
            if dp[day][last] != -1:
                return dp[day][last]
            for i in range(3):
                if i != last:
                    points = max(points , dfs(day + 1 , i) + matrix[day][i])
            dp[day][last] = points

            return points 

        return dfs(0 , -1)
        '''

        for day in range(n-1 , -1 , -1):
            for last in range(-1 , 3):
                points = 0
                for j in range(3):
                    if j != last:
                        points = max(points ,dp[day+1][j+1] + matrix[day][j])
                dp[day][last+1] = points

        
        return dp[0][0] 
