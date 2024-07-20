#User function Template for python3

class Solution:
    def bellman_ford(self, V, edges, S):
        distance = [10**8] * V
        distance[S] = 0
        
        for _ in range(V-1):
            for u, v, w in edges:
                if distance[u] != 10**8 and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
        
        for u, v, w in edges:
            if distance[u] != 10**8 and distance[u] + w < distance[v]:
                return [-1]
        
        return distance



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends