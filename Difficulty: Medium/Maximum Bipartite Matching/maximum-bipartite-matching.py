#User function Template for python3

class Solution:
	def maximumMatch(self, G):
		#code here
		def bpm(u, match, seen):
		    for v in range(N):
		        if G[u][v] and not seen[v]:
		            seen[v] = True
		            if match[v] == -1 or bpm(match[v], match, seen):
		                match[v] = u
		                return True
		    return False
		    
		M = len(G)
		N = len(G[0])
		
		match = [-1] * N
		
		result = 0
		for i in range(M):
            seen = [False] * N
            if bpm(i, match, seen):
                result += 1
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m, n = map(int, input().strip().split())
		G = []
		for i in range(m):
			G.append(list(map(int, input().strip().split())))
		obj = Solution()
		ans = obj.maximumMatch(G)
		print(ans)
# } Driver Code Ends