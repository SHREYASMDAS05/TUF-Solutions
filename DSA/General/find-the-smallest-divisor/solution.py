import math 
class Solution:
    def smallestDivisor(self, nums, limit):
        
        l , r = 1 , max(nums)
        while l <= r:
            m = (l + r) // 2
            total_sum = 0
            for num in nums:
                total_sum += math.ceil(num/m)

            if total_sum <= limit:
                r = m -1
            else:
                l = m + 1

        return l 

       