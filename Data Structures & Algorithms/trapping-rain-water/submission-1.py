class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = [0]
        r_max = [None for i in range(len(height))]
        r_max[-1] = len(height)-1

        for i in range(1, len(height)):
            if height[i]>=height[l_max[-1]]:
                l_max.append(i)
            else:
                l_max.append(l_max[-1])

        for i in range(len(height)-2, -1, -1):
            if height[i]>=height[r_max[i+1]]:
                r_max[i] = i
            else:
                r_max[i] = r_max[i+1]

        output = 0

        for i in range(len(height)):
            output += min(height[l_max[i]], height[r_max[i]]) - height[i]

        return output