#User function Template for python3
from collections import defaultdict

class Solution:
    def DFS(self, adj, u, visited):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                self.DFS(adj, v, visited)

    def isBridge(self, V, adj, c, d):
        # code here
            if c in adj[d]:
                adj[d].remove(c)
            if d in adj[c]:
                adj[c].remove(d)
            else:
                return 0
            
            visited = [False]*V
            
            self.DFS(adj, c, visited)
            
            if not visited[d]:
                return 1
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
            
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        c,d=map(int,input().split())
        ob = Solution()
        
        print(ob.isBridge(V, adj, c,d))
# } Driver Code Ends