class Solution:
    def frogJump(self, heights):
        n = len(heights)
        '''
        dp = [float('inf')] * n
        def dfs(i):
            if i == n -1:
                return 0 
            energy1 = float('inf')
            energy2 = float('inf')
            if dp[i] != float('inf'):
                return dp[i]
            if i + 1 <= n-1:
                energy1 = abs(heights[i] - heights[i+1]) + dfs(i+1)
            if i + 2 <= n-1:
                energy2 = abs(heights[i] - heights[i+2]) + dfs(i+2)
            

            dp[i] =  min(energy1 , energy2)
            return dp[i]

        return dfs(0)
        '''
        '''
        dp = [float('inf')] * (n + 2)
        dp[n-1] = 0
        for i in range(n-2 ,-1 , -1):
            energy1 = float('inf')
            energy2 = float('inf')
            energy1 = abs(heights[i] - heights[i+1]) + dp[i+1]
            if i + 2 <= n-1:
                energy2 = abs(heights[i] - heights[i+2]) + dp[i+2]
            dp[i] = min(energy1 , energy2)

        return dp[0]
        '''
        if n == 1:
            return 0
        prev1 = 0
        prev2 = 0
        for i in range(n-2 , -1 , -1):
            energy1 = float('inf')
            energy2 = float('inf')
            energy1 = abs(heights[i] - heights[i+1]) + prev1
            if i + 2 < n:
                energy2 = abs(heights[i] - heights[i+2]) + prev2
            curr = min(energy1 , energy2)
            prev2 = prev1
            prev1 = curr
        return curr