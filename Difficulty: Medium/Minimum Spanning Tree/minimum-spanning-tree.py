#User function Template for python3
import heapq

class Solution:
    def spanningTree(self, V, adj):
        min_heap = []
        
        visited = [False] * V
        
        heapq.heappush(min_heap, (0, 0))  
        
        total_weight = 0
        edges_in_mst = 0
        
        while min_heap and edges_in_mst < V:
            weight, current_vertex = heapq.heappop(min_heap)
            
            if visited[current_vertex]:
                continue
               
            visited[current_vertex] = True
            total_weight += weight
            edges_in_mst += 1
            
            for neighbor, edge_weight in adj[current_vertex]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
        
        return total_weight

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