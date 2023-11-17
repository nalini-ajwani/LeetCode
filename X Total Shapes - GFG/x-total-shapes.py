

class Solution:
    
    #Function to find the number of 'X' total shapes.
	def xShape(self, grid):
	    def dfs(x, y):
	        if 0 <= x < n and 0 <= y < m and grid[x][y] == 'X':
                grid[x][y] = 'O'
	            dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
                
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X' and not visited[i][j]:
                    count += 1
                    dfs(i, j)
        return count
                    


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = [['#' for i in range(m)] for j in range(n)]
		for i in range(n):
			s = input().strip()
			for j in range(m):
				grid[i][j] = s[j]
		obj = Solution()
		ans = obj.xShape(grid)
		print(ans)
# } Driver Code Ends