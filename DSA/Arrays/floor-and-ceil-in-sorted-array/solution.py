class Solution:
    def getFloorAndCeil(self, nums, x):

        l , r = 0 , len(nums) -1 
        floor = - 1
        ceil = - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == x:
                return [nums[m] ,nums[m]]
            elif nums[m] > x:
                ceil = nums[m]
                r = m - 1
            else:
                floor  = nums[m]
                l = m + 1
        return [floor , ceil]
       
