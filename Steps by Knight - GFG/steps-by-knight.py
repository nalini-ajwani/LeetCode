from collections import deque
class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
	    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
	    sx, sy = KnightPos[0] - 1, KnightPos[1] - 1
	    tx, ty = TargetPos[0] - 1, TargetPos[1] - 1
	    vis = [[False for _ in range(N)] for _ in range(N)]
	    queue = deque([(sx, sy, 0)])
	    vis[sx][sy] = True
	    
	    while queue:
	        x, y, steps = queue.popleft()
	        if x == tx and y == ty:
	            return steps
	        for move in moves:
	            newx, newy = x + move[0], y + move[1]
	            if 0 <= newx < N and 0 <= newy < N and not vis[newx][newy]:
                    queue.append((newx, newy, steps + 1))
                    vis[newx][newy] = True
                    
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