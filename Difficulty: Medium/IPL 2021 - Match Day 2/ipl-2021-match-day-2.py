#User function Template for python3

class Solution:
    def max_of_subarrays(self,arr,n,k):
        '''
        you can use collections module here.
        :param a: given array
        :param n: size of array
        :param k: value of k
        :return: A list of required values 
        '''
        #code here
        res = []
        dq = deque()
        
        for i in range(k):
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
        res.append(arr[dq[0]])
            
        for i in range(k, n):
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            res.append(arr[dq[0]])
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends