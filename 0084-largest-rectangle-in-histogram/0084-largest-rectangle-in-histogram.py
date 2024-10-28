class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s = []
        maxArea = 0
        n = len(heights)
        
        for i in range(n):
            while s and heights[i] < heights[s[-1]]:
                h = heights[s.pop()]
                width = i if not s else i - s[-1] - 1
                maxArea = max(maxArea, h*width)
            s.append(i)
            
        while s:
            h = heights[s.pop()]
            width = n if not s else n - s[-1] - 1
            maxArea = max(maxArea, h * width)
        
        return maxArea