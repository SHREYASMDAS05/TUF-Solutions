class Solution:
    def shipWithinDays(self, weights, days):
        # Your code goes here
        def total_no_days(capacity):
            total_days = 1
            currsum = 0
            for i in range(len(weights) - 1):
                currsum += weights[i]
                if currsum + weights[i+1] > capacity:
                    total_days +=1 
                    currsum = 0
            return total_days <= days

        l , r = max(weights) , sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if total_no_days(mid):
                r = mid -1 
            else:
                l = mid + 1

        return l 
