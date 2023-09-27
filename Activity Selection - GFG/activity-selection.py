#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        act = [(start[i], end[i]) for i in range(n)]
        act.sort(key = lambda x: x[1])
        maxact = 0
        cur_end_time = -1
        
        for a in act:
            stime, etime = a
            if stime > cur_end_time:
                maxact += 1
                cur_end_time = etime
        return maxact


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends