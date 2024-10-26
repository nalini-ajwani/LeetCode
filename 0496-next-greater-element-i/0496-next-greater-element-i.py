class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nextg = {}
        stk = []
        
        for num in reversed(nums2):
            while stk and stk[-1] <= num:
                stk.pop()
            nextg[num] = stk[-1] if stk else -1
            stk.append(num)
            
        return [nextg[num] for num in nums1]