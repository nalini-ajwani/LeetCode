class Solution:
	def isBipartite(self, V, adj):
	    colors = [-1]*V
	    
	    def dfs(node,color):
	        colors[node] = color
	        for n in adj[node]:
	            if colors[n] == -1:
	                if not dfs(n, 1 - color):
	                    return False
	            elif colors[n] == color:
	                return False
	        return True
	            
	    for  i in range(V):
	        if colors[i] == -1:
	            if not dfs(i, 0):
	                return False
	                    
	    return True


#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends