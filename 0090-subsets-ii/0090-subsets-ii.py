class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.backtrack(nums, 0, [], res)
        return res
    
    def backtrack(self, nums, start, path, res):
        res.append(list(path))
            
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
                    
            path.append(nums[i])
            self.backtrack(nums, i+1, path, res)
            path.pop()