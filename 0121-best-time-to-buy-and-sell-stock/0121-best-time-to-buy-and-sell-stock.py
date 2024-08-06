class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxp = 0
        minp = float('inf')
        for i in range(n):
            minp = min(minp, prices[i])
            maxp = max(maxp, prices[i] - minp)
        return maxp
        