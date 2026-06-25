class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        MaxArea = 0
        for i in range (len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] -1
                else:
                    width = i
                MaxArea = max(MaxArea, h*width)
            stack.append(i)
        while stack:
            h = heights[stack.pop()]
            if stack:
                width = len(heights) - stack[-1] -1
            else:
                width = len(heights)
            MaxArea = max( MaxArea, h*width)
        
        return MaxArea