import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        distances = [float('inf')] * V
        distances[S] = 0
        pq = [(0, S)]

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)

           
            for neighbor, weight in adj[current_vertex]:
                new_dist = distances[current_vertex] + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances


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
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends