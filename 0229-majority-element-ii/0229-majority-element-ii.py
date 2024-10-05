class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ele1, ele2 = None, None
        cnt1, cnt2 = 0, 0
        for num in nums:
            if ele1 == num:
                cnt1 += 1
            elif ele2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                ele1, cnt1 = num, 1
            elif cnt2 == 0:
                ele2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
                
        res = []
        cnt1 = nums.count(ele1)
        cnt2 = nums.count(ele2)
        
        if cnt1 > len(nums)//3:
            res.append(ele1)
        if ele1 != ele2 and cnt2 > len(nums)//3:
            res.append(ele2)
            
        return res
        