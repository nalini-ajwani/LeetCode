class Solution(object):
    def arrangeCoins(self, n):
        i=0
        while n>=0:
            i+=1
            n=n-i
        return i-1