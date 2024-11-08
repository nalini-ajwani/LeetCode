class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        cnt = (len(b) + len(a) - 1) // len(a)
        
        if b in a * cnt:
            return cnt
        elif b in a * (cnt + 1):
            return cnt + 1
        return -1