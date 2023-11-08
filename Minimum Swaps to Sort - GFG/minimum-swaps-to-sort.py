

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
	    n = len(nums)
	    arr = [(nums[i], i) for i in range(n)]
	    arr.sort()
	    
	    visited = [False] * n
	    min_swaps = 0
	    
	    for i in range(n):
	        if visited[i] or arr[i][1] == i:
	            continue
	        cycle = 0
	        j = i
	        while not visited[j]:
	            visited[j] = True
	            j = arr[j][1]
	            cycle += 1
	        if cycle > 0:
	           min_swaps += (cycle - 1)
	    return min_swaps       
	   


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends