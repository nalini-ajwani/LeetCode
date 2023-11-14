#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        vis = [False] * V
        pq = [(0,0)]
        result = 0
        
        while pq:
            weight, u = heapq.heappop(pq)
            if vis[u]:
                continue
            vis[u] = True
            result += weight
            
            for v, w in adj[u]:
                if not vis[v]:
                    heapq.heappush(pq, (w, v))
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends