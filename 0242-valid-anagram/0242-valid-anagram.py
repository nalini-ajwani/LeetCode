class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        cntS, cntT = {}, {}
        for i in range(len(s)):
            cntS[s[i]] = 1 + cntS.get(s[i], 0)
            cntT[t[i]] = 1 + cntT.get(t[i], 0)
        for c in cntS:
            if cntS[c] != cntT.get(c, 0):
                return False
        return True