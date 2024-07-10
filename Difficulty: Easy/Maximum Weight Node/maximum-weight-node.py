#User function Template for python3

class Solution():
    def maxWeightCell(self, N, Edge):
        #your code goes here
        weights = [0] * N
        for i in range(N):
            if Edge[i] != -1:
                weights[Edge[i]] += i
                
        max_weight = -1
        max_index = -1
        for i in range(N):
            if weights[i] > max_weight:
                max_weight = weights[i]
                max_index = i
            elif weights[i] == max_weight and i > max_index:
                max_index = i
        
        return max_index


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        obj = Solution()
        ans=obj.maxWeightCell(N, Edge);
        print(ans)

# } Driver Code Ends