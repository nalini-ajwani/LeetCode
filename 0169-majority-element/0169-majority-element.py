class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele, count = 0, 0
        for n in nums:
            if count == 0:
                ele = n
            if n == ele:
                count += 1
            else:
                count -= 1
        return ele
    