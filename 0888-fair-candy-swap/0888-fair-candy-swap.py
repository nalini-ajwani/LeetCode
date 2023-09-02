class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        x = (sum(aliceSizes) - sum(bobSizes))/2
        sets = set(aliceSizes)
        for y in bobSizes:
            if y + x in sets:
                return[y+x, y]