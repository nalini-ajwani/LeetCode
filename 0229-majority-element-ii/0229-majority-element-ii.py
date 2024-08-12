class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        can1, can2 = None, None
        cnt1, cnt2 = 0, 0
        
        for num in nums:
            if can1 == num:
                cnt1 += 1
            elif can2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                can1, cnt1 = num, 1
            elif cnt2 == 0:
                can2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
                
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == can1:
                cnt1 += 1
            elif num == can2:
                cnt2 += 1
                
        res = []
        if cnt1 > len(nums)//3:
            res.append(can1)
        if cnt2 > len(nums)//3:
            res.append(can2)
            
        return res
        