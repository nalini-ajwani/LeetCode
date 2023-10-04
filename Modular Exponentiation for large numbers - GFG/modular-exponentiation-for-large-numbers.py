#User function Template for python3

class Solution:
    def PowMod(self, x, n, M):
        
        if n == 0:
            return 1
        result = 1
        x = x % M
        
        while n > 0:
            if n % 2 == 1:
                result = (result * x) % M
            x = (x * x) % M
            n = n // 2
        
        return result

        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends