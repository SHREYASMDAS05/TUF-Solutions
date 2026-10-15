class Solution:
    def frogJump(self, heights, k):
        n = len(heights)
        dp = [-1] * n
        def dfs(i):
            if i == n-1:
                return 0
            if dp[i] != -1:
                return dp[i]
            energy = float('inf')
            for j in range(i+1 , i + k+1):
                if j < n:
                    energy = min(energy , abs(heights[i]- heights[j]) + dfs(j))
                    dp[i] = energy
            
            return energy
        return dfs(0)

