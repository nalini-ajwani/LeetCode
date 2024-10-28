#User function Template for python3
class Solution:
    def subsetSums(self, arr, n):
        result = []  
        self._findSubsetSums(arr, n, 0, 0, result)
        return result

    def _findSubsetSums(self, arr, n, index, current_sum, result):
        if index == n:
            result.append(current_sum)  
            return
        
        self._findSubsetSums(arr, n, index + 1, current_sum + arr[index], result)
        
        self._findSubsetSums(arr, n, index + 1, current_sum, result)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x, end=" ")
        print("")

# } Driver Code Ends