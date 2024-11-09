class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        split1 = version1.split(".")
        split2 = version2.split(".")
        i = 0
        while i < len(split1) and i < len(split2):
            if int(split1[i]) < int(split2[i]):
                return -1
            if int(split1[i]) > int(split2[i]):
                return 1
            i += 1
            
        while i < len(split1):
            if int(split1[i]) > 0:
                return 1
            i += 1
        while i < len(split2):
            if int(split2[i]) > 0:
                return -1
            i += 1
            
        return 0