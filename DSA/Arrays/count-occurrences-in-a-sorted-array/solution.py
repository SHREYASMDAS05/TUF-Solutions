class Solution:
    def countOccurrences(self, arr, target):
        # Your code goes here
        l , r = 0 , len(arr) -1
        first = -1 
        last = -1 
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                first = m
                r = m - 1
            elif arr[m] > target:
                r = m - 1
            else:
                l = m + 1

        l , r = 0 , len(arr) -1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                last = m
                l = m + 1
            elif arr[m] > target:
                r = m - 1
            else:
                l = m + 1
        if first == -1:
            return 0
        return (last - first + 1)
