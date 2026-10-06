class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #your code goes here
        l , res = 0 , 0 
        max_freq = 0
        hashmap  = {}
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r] , 0) + 1
            max_freq = max(max_freq , hashmap[s[r]])

            while (r - l + 1) - max_freq > k:
                hashmap[s[l]] -= 1
                l += 1
            res = max(res , r-l + 1)
        return res 