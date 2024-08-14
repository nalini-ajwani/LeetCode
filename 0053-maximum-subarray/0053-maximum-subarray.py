import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxm = -sys.maxsize-1
        sumtot = 0
        for i in range(len(nums)):
            sumtot += nums[i]
            if sumtot > maxm:
                maxm = sumtot
            if sumtot < 0:
                sumtot = 0
        return maxm