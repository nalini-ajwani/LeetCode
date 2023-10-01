#User function Template for python3

class Solution:
	def findPeakElement(self, a):
	    l, r = 0, len(a) - 1
	    while l < r:
	        mid = l + (r - l) // 2
	        if a[mid] < a[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return a[l]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		a = list(map(int,input().split()))
		ob = Solution();
		ans = ob.findPeakElement(a)
		print(ans)




# } Driver Code Ends