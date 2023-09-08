class Solution(object):
    def findKthPositive(self, arr, k):
        left = 0
        right = len(arr)
        while left < right:
            middle = (left + right) // 2
            if arr[middle] - middle - 1 < k:
                left = middle + 1
            else:
                right = middle
        return left + k