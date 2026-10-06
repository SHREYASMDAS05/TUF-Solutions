class Solution:
    def totalFruits(self, fruits):
        #your code goes here
        #longest subarray with at most 2 distinct elements.

        l , res  = 0 , 0 
        hashmap = {}

        for r in range(len(fruits)):
            hashmap[fruits[r]] = hashmap.get(fruits[r] , 0 ) + 1

            while len(hashmap) > 2:
                if fruits[l] in hashmap:
                    hashmap[fruits[l]] -= 1
                if hashmap[fruits[l]] == 0 :
                    del hashmap[fruits[l]]
                l += 1

            res = max(res , r-l + 1)

        return res