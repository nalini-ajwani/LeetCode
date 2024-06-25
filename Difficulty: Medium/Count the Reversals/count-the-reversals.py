def countRev(s):
    if len(s) % 2 != 0:
        return -1

    stack = []
    
    unmatched_closing = 0
    
    for char in s:
        if char == '{':
            stack.append(char)
        else:  # char == '}'
            if stack:
                stack.pop()
            else:
                unmatched_closing += 1
    
    unmatched_opening = len(stack)
    
    reversals = (unmatched_opening + 1) // 2 + (unmatched_closing + 1) // 2
    
    return reversals


#{ 
 # Driver Code Starts
t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends