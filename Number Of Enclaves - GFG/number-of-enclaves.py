#User function Template for python3

from typing import List

class Solution:
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                    grid[r][c] = 0
                    for dr, dc in directions:
                        stack.append((r + dr, c + dc))

        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        count = sum(row.count(1) for row in grid)
        return count





#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends