class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        s = []

        for num in reversed(nums2):
            while s and s[-1] <= num:
                s.pop()
            next_greater[num] = s[-1] if s else -1
            s.append(num)
        return [next_greater[n] for n in nums1]