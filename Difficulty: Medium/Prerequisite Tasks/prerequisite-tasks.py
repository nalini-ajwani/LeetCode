#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def isPossible(self,N,P,prerequisites):
        #code here
        adj = defaultdict(list)
        in_deg = [0] * N
        
        for u, v in prerequisites:
            adj[v].append(u)
            in_deg[u] += 1
            
        queue = deque([i for i in range(N) if in_deg[i]==0])
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            
            for neighbor in adj[node]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    queue.append(neighbor)
                    
        return count == N
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,P,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends