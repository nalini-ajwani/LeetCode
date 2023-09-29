#User function Template for python3

class Solution:
    def indexes(self, v, x):
        first_occurrence = self.find_first_occurrence(v, x)
        last_occurrence = self.find_last_occurrence(v, x)
        
        return [first_occurrence, last_occurrence]
    
    def find_first_occurrence(self, v, x):
        left, right = 0, len(v) - 1
        result = -1  
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if v[mid] == x:
                result = mid  
                right = mid - 1  
            elif v[mid] < x:
                left = mid + 1  
            else:
                right = mid - 1  
        
        return result

    def find_last_occurrence(self, v, x):
        left, right = 0, len(v) - 1
        result = -1  
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if v[mid] == x:
                result = mid  
                left = mid + 1  
            elif v[mid] < x:
                left = mid + 1  
            else:
                right = mid - 1  
        
        return result

        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends