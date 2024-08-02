#User function Template for python3
import sys
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        n = len(arr)
        maxx = -sys.maxsize-1
        summ = 0
        
        for i in range(n):
            summ += arr[i]
            
            if summ > maxx:
                maxx = summ
                
            if summ < 0:
                summ = 0
                
        return maxx


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends