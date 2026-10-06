class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #your code goes here
        need = {}
        for ch in t :
            need[ch] = need.get(ch , 0) + 1

        window = {}
        l = 0 
        formed = 0 
        required = len(need)
        res = ''
        res_length = float('inf')

        for r in range(len(s)):
            window[s[r]] = window.get(s[r] , 0) + 1

            if s[r] in need and window[s[r]] == need[s[r]]:
                formed += 1
            while formed == required:
                if r - l + 1 < res_length:
                    res_length = r - l + 1
                    res = s[l:r+1]
                if s[l] in need and window[s[l]] == need[s[l]]:
                    formed -= 1 
                window[s[l]] -= 1
                l+=1

        return res
