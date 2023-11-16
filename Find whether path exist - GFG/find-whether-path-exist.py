
class Solution:
    def is_Possible(self, grid):
        def dfs(x, y):
            visited[x][y] = True

            if grid[x][y] == 2:
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 0 and not visited[nx][ny]:
                    if dfs(nx, ny):
                        return True

            return False

        n = len(grid)
        visited = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return False

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]



#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.is_Possible(grid)
	if(ans):
		print("1")
	else:
		print("0")

# } Driver Code Ends