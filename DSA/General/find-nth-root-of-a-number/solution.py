class Solution:
    def NthRoot(self, n, m):
        l , r = 0 , m 
        while l <= r:
            mid = (l + r) // 2
            if mid**n == m:
                return mid 
            elif mid ** n > m:
                r  = mid -1 
            else:
                l = mid + 1
        return -1

      