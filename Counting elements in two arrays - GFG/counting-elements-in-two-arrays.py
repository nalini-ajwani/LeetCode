#User function Template for python3
class Solution:
    def countEleLessThanOrEqual(self, arr1, n1, arr2, n2):
        arr2.sort()
        
        res = []
        for i in range(n1):
            count = self.binary_search(arr2, n2, arr1[i])
            res.append(count)
        
        return res

    def binary_search(self, arr, n, target):
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1,n2=[int(x) for x in input().split()]
        arr1=[int(x) for x in input().split()]
        arr2=[int(x) for x in input().split()]
    
        res = Solution().countEleLessThanOrEqual(arr1,n1,arr2,n2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends