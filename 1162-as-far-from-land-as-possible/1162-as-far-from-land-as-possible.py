from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        
        if len(q) == 0 or len(q) == n*n:
            return -1
        
        maxdist = -1
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        
        while q:
            x, y = q.popleft()
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = grid[x][y] + 1
                    maxdist = grid[nx][ny] - 1
                    q.append((nx, ny))
        return maxdist