class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for l in range(len(nums)-k+1):
            mx = -100000
            for r in range(l, l+k):
                mx = max(mx, nums[r])
            output.append(mx)
        return output