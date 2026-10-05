class Solution:
    def findMin(self, nums):
        l , r = 0 , len(nums) - 1

        while l < r:
            m = (l + r) // 2
            #min in right sorted array 
            if nums[m] > nums[r]:
                l = m + 1
            #min is at m or left sorted 
            else:
                r = m 

        return nums[l]
            
                
