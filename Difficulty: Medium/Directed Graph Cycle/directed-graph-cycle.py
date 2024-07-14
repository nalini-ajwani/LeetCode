#User function Template for python3
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        def dfs(v, vis, rec):
            vis[v] = True
            rec[v] = True
            for n in adj[v]:
                if not vis[n]:
                    if dfs(n, vis, rec):
                        return True
                elif rec[n]:
                    return True
            rec[v] = False
            return False
            
        vis = [False] * V
        rec = [False] * V
        for v in range(V):
            if not vis[v]:
                if dfs(v, vis, rec):
                    return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

# } Driver Code Ends