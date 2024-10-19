#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        vis = [False] * V
        stk = []
        
        def dfs(v):
            vis[v] = True
            for n in adj[v]:
                if not vis[n]:
                    dfs(n)
            stk.append(v)
            
        for i in range(V):
            if not vis[i]:
                dfs(i)
                
        transpose = [[] for _ in range(V)]
        for i in range(V):
            for n in adj[i]:
                transpose[n].append(i)
                
        visited = [False] * V  # Reset visited array for second DFS
        scc_count = 0
        
        def reverse_dfs(v):
            visited[v] = True
            for neighbor in transpose[v]:
                if not visited[neighbor]:
                    reverse_dfs(neighbor)
        
        while stk:
            v = stk.pop()  
            if not visited[v]:  
                reverse_dfs(v)  
                scc_count += 1  
        
        return scc_count


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
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends