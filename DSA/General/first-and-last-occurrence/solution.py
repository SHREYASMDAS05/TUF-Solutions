class Solution:
    def searchRange(self, nums, target):
        l , r  = 0 , len(nums) - 1
        first , last = -1 , -1 
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                first = m
                r = m - 1
            elif nums[m] > target:
                r = m -1 

            else:
                l = m + 1

        l , r  = 0 , len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                last = m
                l = m + 1

            elif nums[m] > target:
                r = m -1 

            else:
                l = m + 1

        return [first , last]
        
        