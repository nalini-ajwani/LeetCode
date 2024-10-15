from collections import deque
class Solution:
	def isBipartite(self, V, adj):
		#code here
		color = [-1] * V
		
		def bfs(src):
		    q = deque([src])
		    color[src] = -1
		    while q:
		        node = q.popleft()
		        for n in adj[node]:
		            if color[n] == -1:
		                color[n] = 1 - color[node]
		                q.append(n)
		            elif color[n] == color[node]:
		                return False
		    return True
		            
	    for i in range(V):
	        if color[i] == -1:
	            if not bfs(i):
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