class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = [0]*(len(height))
        r_max = [0]*(len(height))
        l_max[0] = height[0]
        r_max[-1] = height[-1]
        output = 0

        for i in range(1, len(height)):
            l_max[i] = max(height[i],l_max[i-1])
        
        for i in range(len(height)-2, -1, -1):
            r_max[i] = max(height[i],r_max[i+1])
            curr = min(l_max[i], r_max[i])
            output += curr - height[i]
        
        return output