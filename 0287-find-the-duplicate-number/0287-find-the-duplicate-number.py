class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq = [0] * (n+1)
        for i in range(n):
            if freq[nums[i]] == 0:
                freq[nums[i]] += 1
            else:
                return nums[i]
        return 0
        