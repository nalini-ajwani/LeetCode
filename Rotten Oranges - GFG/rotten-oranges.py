from collections import deque

class Solution:
    def orangesRotting(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        fresh_oranges, rotten = 0, deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0

        # BFS to rot oranges
        while rotten and fresh_oranges:
            size = len(rotten)
            for _ in range(size):
                x, y = rotten.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        rotten.append((nx, ny))

            minutes += 1

        return -1 if fresh_oranges != 0 else minutes



#{ 
 # Driver Code Starts
from queue import Queue


T=int(input())
for i in range(T):
	n, m = map(int, input().split())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.orangesRotting(grid)
	print(ans)

# } Driver Code Ends