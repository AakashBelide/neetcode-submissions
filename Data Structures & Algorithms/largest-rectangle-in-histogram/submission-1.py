class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []

        for i in range(n):
            popped_ind = -1
            while stack and stack[-1][1]>heights[i]:
                popped_ind, popped_height = stack.pop()
                max_area = max(max_area, popped_height*(i-popped_ind))
            if popped_ind>-1:
                stack.append([popped_ind, heights[i]])
            else:
                stack.append([i, heights[i]])
        
        while stack:
            popped_ind, popped_height = stack.pop()
            max_area = max(max_area, popped_height*(n-popped_ind))
        
        return max_area