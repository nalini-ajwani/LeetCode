#User function Template for python3

class Solution:
    def celebrity(self, M, n):
        candidate = 0
        for i in range(1, n):
            if M[candidate][i] == 1:
                candidate = i
        
        for i in range(n):
            if i != candidate and (M[candidate][i] == 1 or M[i][candidate] == 0):
                return -1
        
        return candidate



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends