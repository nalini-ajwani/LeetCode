class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxsofar = nums[0]
        maxend = nums[0]
        for num in nums[1:]:
            maxend = max(num, maxend+num)
            maxsofar = max(maxsofar, maxend)
        return maxsofar