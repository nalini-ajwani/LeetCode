#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        """
        :type k: int
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        def kth_helper(k, start1, start2):
            # Base cases
            if start1 >= len(arr1):
                return arr2[start2 + k - 1]
            if start2 >= len(arr2):
                return arr1[start1 + k - 1]
            if k == 1:
                return min(arr1[start1], arr2[start2])
            
            idx1 = start1 + k // 2 - 1
            idx2 = start2 + k // 2 - 1
            
            val1 = arr1[idx1] if idx1 < len(arr1) else float('inf')
            val2 = arr2[idx2] if idx2 < len(arr2) else float('inf')
            
            if val1 < val2:
                return kth_helper(k - k // 2, idx1 + 1, start2)
            else:
                return kth_helper(k - k // 2, start1, idx2 + 1)
        
        return kth_helper(k, 0, 0)

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends