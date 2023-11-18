#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        def dfs(node, visited):
            visited[node] = True
            for neighbor in range(V):
                if adj[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor, visited)

        provinces = 0
        visited = [False] * V

        for i in range(V):
            if not visited[i]:
                provinces += 1
                dfs(i, visited)

        return provinces


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends