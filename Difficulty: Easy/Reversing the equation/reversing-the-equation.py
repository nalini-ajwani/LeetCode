#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        numbers = []
        operators = []
        
        i = 0
        n = len(s)
        
        while i < n:
            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                numbers.append(num)
            else:
                operators.append(s[i])
                i += 1
        
        numbers.reverse()
        operators.reverse()
        
        result = []
        num_index = 0
        op_index = 0
        for j in range(len(s)):
            if s[j].isdigit():
                if j == 0 or not s[j-1].isdigit():
                    result.append(str(numbers[num_index]))
                    num_index += 1
            else:
                result.append(operators[op_index])
                op_index += 1
        
        return ''.join(result)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends