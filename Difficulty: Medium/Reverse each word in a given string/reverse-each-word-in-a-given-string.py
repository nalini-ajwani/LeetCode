#User function Template for python3

class Solution:
    def reverseWords(self, s):
        # code here
        w = s.split('.')
        rev = [word[::-1] for word in w]
        res = '.'.join(rev)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends