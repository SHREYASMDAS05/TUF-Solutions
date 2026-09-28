class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        max_length = 0 
        for n in nums:
            if n-1 not in nums:
                length = 0
                while (n + length) in nums :
                    length += 1
                max_length = max(max_length , length)

        return max_length