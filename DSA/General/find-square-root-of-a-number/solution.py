class Solution:
    def floorSqrt(self, n: int) -> int:
        l , r = 0 , n 
        while l <= r:
            m = (l + r) // 2
            if m**2 == n:
                return m 
            elif m ** 2 > n:
                r  = m -1 
            else:
                l = m + 1
        return l -1

