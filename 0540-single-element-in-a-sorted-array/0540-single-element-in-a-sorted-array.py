class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)// 2
            if mid % 2 == 1:
                mid -= 1
                
            if nums[mid] != nums[mid+1]:
                r = mid
            else:
                l = mid + 2
        return nums[l]