class Solution:
    def nonAdjacent(self, nums):
        n = len(nums)
        '''
        dp =  [-1] * (n)
        def dfs(i):
            if i >= n:
                return 0 
            if dp[i] != -1:
                return dp[i]   
            return max(dfs(i+1) , nums[i] + dfs(i+2))

        return dfs(0)
        dp =  [0] * (n+2)
        for i in range(n-1 , -1 , -1):
                dp[i] = max(dp[i+1] , nums[i] + dp[i+2])

        return dp[0]
        '''
        prev1 = 0 
        prev2 = 0 
        for i in range(n-1 , -1 , -1):
            curr = max(prev1 , prev2 + nums[i])
            prev2 = prev1
            prev1 = curr

        return curr
        
