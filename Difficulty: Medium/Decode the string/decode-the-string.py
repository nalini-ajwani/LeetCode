#User function Template for python3

class Solution:
    def decodedString(self, s):
        count_stack = []
        result_stack = []
        
        # Current values
        current_num = 0
        current_string = ''
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                count_stack.append(current_num)
                result_stack.append(current_string)
                
                current_num = 0
                current_string = ''
            elif char == ']':
                repeat_times = count_stack.pop()
                last_string = result_stack.pop()
                current_string = last_string + current_string * repeat_times
            else:
                current_string += char
        
        return current_string



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends