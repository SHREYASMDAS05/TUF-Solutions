class Solution:
    def subarraySum(self, nums, k):
        currsum = 0 
        res = 0 
        hashmap = {0:1}
        for n in nums:
            currsum += n 
            diff = currsum - k 
            if diff in hashmap:
                res += hashmap[diff]
            hashmap[currsum] = hashmap.get(currsum, 0) + 1

        return res 

      