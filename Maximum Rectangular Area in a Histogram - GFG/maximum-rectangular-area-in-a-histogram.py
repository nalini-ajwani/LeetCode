#User function Template for python3


class Solution:
    def getMaxArea(self, histogram):
        stack = []  
        max_area = 0  
        i = 0  

        while i < len(histogram):
            if not stack or histogram[i] >= histogram[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top_of_stack = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                area = histogram[top_of_stack] * width
                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()
            width = i if not stack else len(histogram) - stack[-1] - 1
            area = histogram[top_of_stack] * width
            max_area = max(max_area, area)

        return max_area



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends