# User function Template for Python3

class Solution:
    def maxLength(self, S):
        s = []
        maxL = 0
        start = -1
        for i in range(len(S)):
            if S[i] == '(':
                s.append(i)
            else:
                if not s:
                    start = i
                else:
                    s.pop()
                    if not s:
                        maxL = max(maxL, i - start)
                    else:
                        maxL = max(maxL, i - s[-1])
                        
        return maxL


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends