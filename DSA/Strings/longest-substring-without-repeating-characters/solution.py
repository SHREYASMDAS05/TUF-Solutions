class Solution:
    def longestNonRepeatingSubstring(self, s):
        #your code goes here
        res = 0
        hashmap = {}
        l , r = 0 , 0 
        while r < len(s):
            if s[r] in hashmap:
                l = max( l , hashmap[s[r]] + 1)
                hashmap[s[r]] = r
            else:
                hashmap[s[r]] = r
            res = max(res , r-l + 1)
            r += 1
        return res
            

