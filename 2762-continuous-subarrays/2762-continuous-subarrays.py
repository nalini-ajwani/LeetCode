class Solution(object):
    def continuousSubarrays(self, nums):
        maxQ = deque()
        minQ = deque()
        l = 0
        res = 0
        for right in range(len(nums)):
            while maxQ and nums[maxQ[-1]] < nums[right]:
                maxQ.pop()
            maxQ.append(right)

            while minQ and nums[minQ[-1]] > nums[right]:
                minQ.pop()
            minQ.append(right)

            while nums[maxQ[0]] - nums[minQ[0]] > 2:
                if maxQ[0] < minQ[0]:
                    l = maxQ[0] + 1
                    maxQ.popleft()
                else:
                    l = minQ[0] + 1
                    minQ.popleft()

            res += right - l + 1
        return res
    