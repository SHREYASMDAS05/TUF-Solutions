class Solution:
    def minimumRateToEatBananas(self, nums, h):
        def total_time(k):
            time = 0 
            for pile in nums:
                time += (pile -1) // k + 1
            return time 

        l , r = 1 , max(nums)
        while l <= r:
            m = (l + r)//2 
            time = total_time(m)
            if time <= h:
                r = m -1 
            else:
                l = m + 1

        return l 

        
            


       