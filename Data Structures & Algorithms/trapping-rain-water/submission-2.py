class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0

        i = 0
        j = len(height) - 1

        leftMax = 0
        rightMax = 0

        while i<j:
            if height[i]<height[j]:
                leftMax = max(leftMax, height[i])
                output += leftMax - height[i]
                i += 1
            else:
                rightMax = max(rightMax, height[j])
                output += rightMax - height[j]
                j -= 1

        return output