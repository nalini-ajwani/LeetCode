#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        def isCyclicUtil(node, visited, recStack):
            visited[node] = True
            recStack[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if isCyclicUtil(neighbor, visited, recStack):
                        return True
                elif recStack[neighbor]:
                    return True

            recStack[node] = False
            return False

        visited = [False] * V
        recStack = [False] * V

        for node in range(V):
            if not visited[node]:
                if isCyclicUtil(node, visited, recStack):
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
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends