class Solution(object):
    def maxSubarraySumCircular(self, nums):
        gMax, gMin = nums[0], nums[0]
        curmax, curmin = 0, 0
        total = 0
        
        for n in nums:
            curmax = max(curmax + n, n)
            curmin = min(curmin + n, n)
            total+= n
            gMax = max(gMax, curmax)
            gMin = min(gMin, curmin)
            
        return max(gMax, total - gMin) if gMax > 0 else gMax
        