class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0

        i = 0
        j = len(height) - 1

        leftMax = height[i]
        rightMax = height[j]

        while i<j:
            if leftMax<rightMax:
                i += 1
                leftMax = max(leftMax, height[i])
                output += leftMax - height[i]
            else:
                j -= 1
                rightMax = max(rightMax, height[j])
                output += rightMax - height[j]

        return output