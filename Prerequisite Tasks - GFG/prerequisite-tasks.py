#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def isPossible(self, N, P, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * N

        for pair in prerequisites:
            task, prerequisite = pair
            graph[prerequisite].append(task)
            in_degree[task] += 1

        queue = deque([task for task in range(N) if in_degree[task] == 0])

        while queue:
            current_task = queue.popleft()
            for neighbor in graph[current_task]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return all(in_degree[task] == 0 for task in range(N))

    


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