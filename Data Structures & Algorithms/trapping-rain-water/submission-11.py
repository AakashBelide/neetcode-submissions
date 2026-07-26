class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_max, r_max = height[l], height[r]
        output = 0

        while l<r:
            if l_max<r_max:
                l += 1
                l_max = max(height[l], l_max)
                output += l_max - height[l]
            else:
                r -= 1
                r_max = max(height[r], r_max)
                output += r_max - height[r]
        return output