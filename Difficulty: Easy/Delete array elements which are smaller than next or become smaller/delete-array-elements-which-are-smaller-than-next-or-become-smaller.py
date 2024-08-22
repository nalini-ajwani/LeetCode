#User function Template for python3

class Solution:
    def deleteElement(self,arr,k):
        stack = []
    
        for num in arr:
            while stack and k > 0 and stack[-1] < num:
                stack.pop()
                k -= 1
            stack.append(num)
        return stack
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.deleteElement(arr, k)
        print(*ans)
        tc -= 1
# } Driver Code Ends