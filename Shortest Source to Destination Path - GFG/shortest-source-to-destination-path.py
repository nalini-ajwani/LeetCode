#User function Template for python3
from collections import deque

class Solution:
    def shortestDistance(self, N, M, A, X, Y):
        if A[0][0] == 0 or A[X][Y] == 0:
            return -1 

        visited = [[False] * M for _ in range(N)]
        queue = deque([(0, 0, 0)])

        while queue:
            current = queue.popleft()
            x, y, steps = current

            if x == X and y == Y:
                return steps  

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < N and 0 <= new_y < M and A[new_x][new_y] == 1 and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, steps + 1))

        return -1  



#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends