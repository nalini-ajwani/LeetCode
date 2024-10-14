class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, island):
            # Mark the cell as visited by adding it to the island list
            grid[i][j] = 2  # marking the island's cells with 2 to distinguish it
            island.append((i, j))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1:
                    dfs(ni, nj, island)

        def bfs(queue):
            steps = 0
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                            if grid[ni][nj] == 1:
                                return steps
                            elif grid[ni][nj] == 0:
                                grid[ni][nj] = 2
                                queue.append((ni, nj))
                steps += 1
            return -1

        # Step 1: Find the first island using DFS
        island1 = []
        found = False
        for i in range(len(grid)):
            if found:
                break
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j, island1)
                    found = True
                    break

        # Step 2: Perform BFS to find the shortest bridge to the second island
        queue = deque(island1)  # Start BFS from all the cells of the first island
        return bfs(queue)
        