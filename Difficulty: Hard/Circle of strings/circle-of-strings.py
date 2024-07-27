#User function Template for python3
from collections import defaultdict
class Solution:
    def isCircle(self, N, A):
        # code here
        in_deg = defaultdict(int)
        out_deg = defaultdict(int)
        
        graph = defaultdict(list)
        
        for word in A:
            start = word[0]
            end = word[-1]
            graph[start].append(end)
            out_deg[start] += 1
            in_deg[end] += 1
            
        for char in set(in_deg.keys()).union(set(out_deg.keys())):
            if in_deg[char] != out_deg[char]:
                return 0
                
        def dfs(node, vis, graph):
            vis.add(node)
            for n in graph[node]:
                if n not in vis:
                    dfs(n, vis, graph)
                    
        vis = set()
        startnode = next((char for char in graph if graph[char]), None)
        if startnode:
            dfs(startnode, vis, graph)
        for char in graph:
            if graph[char] and char not in vis:
                return 0
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        A = input().split()
        
        ob = Solution()
        print(ob.isCircle(N, A))
# } Driver Code Ends