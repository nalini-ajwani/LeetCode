#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        # code here 
        stack = [-1]
        maxLen = 0
        
        for i, char in enumerate(S):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[-1])
        return maxLen


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends