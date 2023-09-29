#User function Template for python3


#Complete this function
import math
class Solution:
    def floorSqrt(self, x): 
        if (x == 0 or x == 1):
            return x
        i = 1
        result = 1
        while (result <= x):
 
            i += 1
            result = i * i
 
        return i - 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends