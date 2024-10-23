class Solution:
    
    def isValid(self, arr, n, m, max_pages):
        student_count = 1
        current_sum = 0
        
        for i in range(n):
            if current_sum + arr[i] > max_pages:
                student_count += 1
                current_sum = arr[i]
                if student_count > m:  
                    return False
            else:
                current_sum += arr[i]
        
        return True
    
    def findPages(self, n, arr, m):
        if m > n:
            return -1
        
        low = max(arr)  
        high = sum(arr)  
        
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.isValid(arr, n, m, mid):
                result = mid
                high = mid - 1  
            else:
                low = mid + 1  
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        m = int(input())

        ob = Solution()

        print(ob.findPages(n, arr, m))

# } Driver Code Ends