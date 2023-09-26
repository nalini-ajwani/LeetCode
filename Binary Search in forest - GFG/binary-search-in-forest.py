import math
class Solution:
    def find_height(self,tree,n,k):
        left, right = 0, max(tree)
        while left < right:
            mid = (left + right) // 2
            total_wood = 0 
            for tree_i in tree:
                if tree_i > mid:
                    total_wood += tree_i - mid
            
            if total_wood == k:
                return mid
            elif total_wood < k:
                right = mid
            else:
                left = mid + 1
        return -1

#{ 
 # Driver Code Starts

t = int(input())
for _ in range(t):
    n = int(input())
    tree = [ int(x) for x in input().strip().split() ]
    k = int(input())
    ob=Solution()
    print(ob.find_height(tree,n,k))
# } Driver Code Ends