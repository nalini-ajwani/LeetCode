

class Solution:

    #Function to find unit area of the largest region of 1s.
	def findMaxArea(self, grid):
	    if not grid or not grid[0]:
	        return 0
	        
	    def dfs(row,col):
	        if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
	            grid[row][col] = 0
	            size = 1
	            for dr in [-1,0,1]:
	                for dc in [-1,0,1]:
	                    size += dfs(row+dr, col+dc)
	            return size
	        return 0
	        
	    rows, cols = len(grid), len(grid[0])
	    max_ar = 0
	    
	    for r in range(rows):
	        for c in range(cols):
	            if grid[r][c] == 1:
	               max_ar = max(max_ar, dfs(r,c)) 
	    return max_ar



#{ 
 # Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.findMaxArea(grid)
        print(ans)

# } Driver Code Ends