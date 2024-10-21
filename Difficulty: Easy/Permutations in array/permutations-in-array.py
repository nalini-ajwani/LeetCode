#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    def isPossible(self, k, arr1, arr2):
        #Your code goes here.
        n = len(arr1)
        arr1.sort(reverse = True)
        arr2.sort()
        for i in range(n):
            if (arr1[i] + arr2[i] < k):
                return False
        return True

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())
    for _ in range(t):
        k = int(input().strip())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.isPossible(k, arr1, arr2)
        if ans:
            print("true")
        else:
            print("false")

if __name__ == "__main__":
    main()
# } Driver Code Ends