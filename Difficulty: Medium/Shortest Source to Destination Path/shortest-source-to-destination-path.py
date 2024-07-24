#User function Template for python3

from collections import deque

class Solution:
    def shortestDistance(self, N, M, A, X, Y):
        if A[0][0] == 0 or A[X][Y] == 0:
            return -1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(0, 0, 0)]) 
        visited = [[False] * M for _ in range(N)]
        visited[0][0] = True

        while queue:
            row, col, steps = queue.popleft()
            if row == X and col == Y:
                return steps
            
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < N and 0 <= newCol < M and not visited[newRow][newCol] and A[newRow][newCol] == 1:
                    visited[newRow][newCol] = True
                    queue.append((newRow, newCol, steps + 1))
        
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