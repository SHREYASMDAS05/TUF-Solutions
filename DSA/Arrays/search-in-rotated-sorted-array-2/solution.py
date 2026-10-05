class Solution:
    def searchInARotatedSortedArrayII(self, nums, k):
        l , r = 0 , len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == k:
                return True
            elif nums[m] < nums[l]:
                if nums[m]< k <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] > nums[l]:
                if nums[l] <= k < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                l = l + 1
        return False