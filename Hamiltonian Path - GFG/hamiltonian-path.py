#User function Template for python3
class Solution:
    def check(self, N, M, Edges):
        graph = {}
        
        for u, v in Edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

        def is_valid(v, pos, path):
            if path[pos - 1] == -1:
                return False

            for vertex in graph[path[pos - 1]]:
                if vertex == v and path.count(v) == 0:
                    return True

            return False

        def hamiltonian_util(path, pos):
            if pos == N:
                return True

            for v in graph[path[pos - 1]]:
                if is_valid(v, pos, path):
                    path[pos] = v
                    if hamiltonian_util(path, pos + 1):
                        return True
                    path[pos] = -1

            return False

        for i in range(1, N + 1):
            path = [-1] * N
            path[0] = i
            
            if hamiltonian_util(path, 1):
                return 1 

        return 0  



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends