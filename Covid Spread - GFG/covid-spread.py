#User function Template for python3
from collections import deque
class Solution:
    def helpaterp(self, hospital):
        rows, cols = len(hospital), len(hospital[0])
        dir = [(1,0) , (-1,0), (0, 1), (0, -1)]
        queue = deque()
        
        for i in range(rows):
            for j in range(cols):
                if hospital[i][j] == 2:
                    queue.append((i, j, 0))
                    
        while queue:
            i, j, time = queue.popleft()
            
            for di, dj in dir:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < rows and 0 <= nj < cols and hospital[ni][nj] == 1:
                    hospital[ni][nj] = 2
                    queue.append((ni, nj, time + 1))
                    
        for i in range(rows):
            for j in range(cols):
                if hospital[i][j] == 1:
                    return -1
        return time
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        
        rc=input().split() #row and column
        r=int(rc[0])    
        c=int(rc[1])
        
        
        hospital=[]
        
        for i in range(r):
            hospital.append([int(j) for j in input().split()])
            
        ob = Solution()        
        print(ob.helpaterp(hospital))

# } Driver Code Ends