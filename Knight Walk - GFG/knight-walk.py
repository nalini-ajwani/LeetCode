from collections import deque
class Solution:
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
	    moves = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (-2, 1), (-1, 2), (1, 2), (2, 1)
        ]

        # Convert positions to 0-based indexing
        start = (KnightPos[0] - 1, KnightPos[1] - 1)
        target = (TargetPos[0] - 1, TargetPos[1] - 1)

        # Initialize a visited array to keep track of visited positions
        visited = [[False] * N for _ in range(N)]

        # Initialize the queue for BFS
        queue =
        deque([(start, 0)])  # (position, steps)
        visited[start[0]][start[1]] = True

        while queue:
            current, steps = queue.popleft()

            if current == target:
                return steps

            # Explore possible moves
            for move in moves:
                new_x, new_y = current[0] + move[0], current[1] + move[1]

                # Check if the new position is valid and not visited
                if 0 <= new_x < N and 0 <= new_y < N and not visited[new_x][new_y]:
                    queue.append(((new_x, new_y), steps + 1))
                    visited[new_x][new_y] = True

        # If the target cannot be reached
        return -1


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	N = int(input())
	KnightPos = list(map(int, input().split()))
	TargetPos = list(map(int, input().split()))
	obj = Solution()
	ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
	print(ans)

# } Driver Code Ends