class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    originalCol = image[sr][sc]
	    if originalCol != newColor:
	        self.dfs(image, sr, sc, originalCol, newColor)
	    return image
	    
	def dfs(self, image, row, col, originalCol, newCol):
	    if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == originalCol:
	        image[row][col] = newCol
	        
	        self.dfs(image, row + 1, col, originalCol, newCol)
	        self.dfs(image, row - 1, col, originalCol, newCol)
	        self.dfs(image, row, col + 1, originalCol, newCol)
	        self.dfs(image, row, col - 1, originalCol, newCol)
	            



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()
# } Driver Code Ends