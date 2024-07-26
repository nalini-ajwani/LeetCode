#User function Template for python3
from collections import defaultdict
class Solution:
    def check(self, N, M, Edges): 
        #code here
        graph = defaultdict(list)
        for u, v in Edges:
            graph[u].append(v)
            graph[v].append(u)
            
        vis = [False] * (N+1)
        path = []
        
        def dfs(node):
            vis[node] = True
            path.append(node)
            
            if len(path) == N:
                return True
                
            for neighbor in graph[node]:
                if not vis[neighbor]:
                    if dfs(neighbor):
                        return True
                        
            vis[node] = False
            path.pop()
            return False
        for start in range(1, N + 1):
            if dfs(start):
                return 1
        
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends