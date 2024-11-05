import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minheap = nums[:k]
        heapq.heapify(minheap)
        
        for num in nums[k:]:
            if num > minheap[0]:
                heapq.heapreplace(minheap, num)
        return minheap[0]