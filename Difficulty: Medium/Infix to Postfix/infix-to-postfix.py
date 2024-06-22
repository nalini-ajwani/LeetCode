#User function Template for python3


class Solution:
    
    # Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        def precedence(op):
            if op == '^':
                return 3
            if op == '*' or op == '/':
                return 2
            if op == '+' or op == '-':
                return 1
            return 0
        
        def infix_to_postfix(expression):
            output = []
            stack = []
            
            for char in expression:
                if char.isalnum():
                    output.append(char)
                elif char == '(':
                    stack.append(char)
                elif char == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop() 
                else:
                    while (stack and precedence(stack[-1]) >= precedence(char)):
                        output.append(stack.pop())
                    stack.append(char)
            
            
            while stack:
                output.append(stack.pop())
            
            return ''.join(output)
        
        return infix_to_postfix(exp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends