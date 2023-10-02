#User function Template for python3

class Solution:
    def leastWeightCapacity(self, arr, N, D):
        left, right = max(arr), sum(arr)

        while left < right:
            mid = left + (right - left) // 2
            days_required = self.calculateDays(arr, mid)

            if days_required > D:
                left = mid + 1
            else:
                right = mid

        return left

    def calculateDays(self, arr, capacity):
        days_required = 1
        current_capacity = 0

        for weight in arr:
            if current_capacity + weight > capacity:
                days_required += 1
                current_capacity = 0

            current_capacity += weight

        return days_required



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        D=int(input())
        
        ob = Solution()
        print(ob.leastWeightCapacity(arr,N,D))
# } Driver Code Ends