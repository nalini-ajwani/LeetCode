class Solution(object):
    def searchRange(self, nums, target):
        l = self.search(nums, target, 0)
        r = self.search(nums, target, 1)
        return [l,r]
    
    def search(self, nums, target, side):            
        
        l, r = 0, len(nums) - 1
        index = -1
        while l <= r:
            mid = (l + r)//2                
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                index = mid
                if side == 0:
                    r = mid - 1
                else:
                    l = mid + 1
        return index