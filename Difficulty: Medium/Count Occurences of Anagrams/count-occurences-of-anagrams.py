#User function Template for python3
from collections import Counter

class Solution:
    def search(self, pat, txt):
        m = len(pat)
        n = len(txt)
        
        if m > n:
            return 0
            
        patcount = Counter(pat)
        window = Counter(txt[:m]) 
        
        count = 0
        
        if patcount == window:
            count += 1
            
        for i in range(m, n):
            window[txt[i]] += 1
            
            old = txt[i - m]
            if window[old] == 1:
                del window[old]
            else:
                window[old] -= 1
                
            if patcount == window:
                count += 1
        
        return count
	        
	   


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends