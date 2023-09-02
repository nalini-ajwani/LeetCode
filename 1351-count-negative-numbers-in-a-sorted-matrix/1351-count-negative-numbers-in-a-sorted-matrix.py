class Solution(object):
    def countNegatives(self, grid):
        rows, cols = len(grid), len(grid[0])
        negative = 0
        col = 0
        for row in range(rows - 1, -1, -1):
            while col < cols and grid[row][col] >= 0:
                col += 1
            negative += cols - col
        return negative