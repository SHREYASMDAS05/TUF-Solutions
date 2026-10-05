class Solution:
    def roseGarden(self, n, nums, k, m):
        #your code goes here
        if n < k * m:
            return -1 
        def possible(day):
            flowers = 0 
            bouquets = 0
            for i in nums:
                if i <= day:
                    flowers +=1 
                    if flowers == k :
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0 

            return bouquets >= m

        l ,r = 1 , max(nums)

        while l <= r:
            mid = (l + r) // 2
            if possible(mid):
                r = mid -1
            else:
                l  = mid + 1

        return l 
