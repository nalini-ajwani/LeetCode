#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        from collections import Counter
        if not p or not s:
            return "-1"
            
        pcount = Counter(p)
        req = len(pcount)
        
        window = Counter()
        l, r = 0, 0
        formed = 0
        minlen = float('inf')
        minwin = ""
        
        while r < len(s):
            char = s[r]
            window[char] += 1
            
            if char in pcount and window[char] == pcount[char]:
                formed += 1
                
            while l <= r and formed == req:
                char = s[l]
                if (r-l+1) < minlen:
                    minlen = r-l+1
                    minwin = s[l:r+1]
                    
                window[char] -= 1
                if char in pcount and window[char] < pcount[char]:
                    formed -= 1
                    
                l += 1
            r += 1
            
        return minwin if minwin else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends