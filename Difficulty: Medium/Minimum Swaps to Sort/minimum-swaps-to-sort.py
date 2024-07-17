

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		n = len(nums)
		arr = [(num, i) for i, num in enumerate(nums)]
		arr.sort()
		vis = [False] * n
		swap = 0
		for i in range(n):
		    if vis[i] or arr[i][1] == i:
		        continue
		    cycle = 0
		    j = i
		    while not vis[j]:
		        vis[j] = True
		        j = arr[j][1]
		        cycle += 1
		    if cycle > 0:
		        swap += (cycle - 1)
		return swap


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