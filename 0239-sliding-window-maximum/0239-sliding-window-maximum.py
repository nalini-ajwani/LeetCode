from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        dq = deque()
        
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
                
            if dq and dq[0] < i -k + 1:
                dq.popleft()
                
            dq.append(i)
            
            if i >= k-1:
                res.append(nums[dq[0]])
                
        return res