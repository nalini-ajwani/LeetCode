#User function Template for python3
class Solution:
    def bracketNumbers(self, s):
        stack = []
        result = []
        counter = 1

        for char in s:
            if char == '(':
                stack.append(counter)
                result.append(counter)
                counter += 1
            elif char == ')':
                result.append(stack.pop())

        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends