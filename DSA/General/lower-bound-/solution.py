class Solution:
    def lowerBound(self, nums, x):
        l ,r = 0 , len(nums) -1 
        ans = len(nums)

        while l <= r :
            m = (l + r) // 2
            if nums[m] >= x:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
       


