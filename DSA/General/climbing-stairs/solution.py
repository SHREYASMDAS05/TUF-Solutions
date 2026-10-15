class Solution:
    def climbStairs(self, n):
        '''
        def dfs(i):
            if i == 0:
                return 1
            if i < 0:
                return 0 
            res = 0 
            res += dfs(i-1) + dfs(i-2)
            return res
        return dfs(n)
        '''
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2 ,n+1):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
