#User function Template for python3

class Solution:
    def delHelper(self, stack, curIdx, midIdx):
        if curIdx == midIdx:
            stack.pop()
            return
        top = stack.pop()
        self.delHelper(stack, curIdx + 1, midIdx)
        stack.append(top)
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        if sizeOfStack == 0:
            return 
        midEle = sizeOfStack // 2
        self.delHelper(s, 0, midEle)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
sys.setrecursionlimit(10**8)

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
    
# } Driver Code Ends