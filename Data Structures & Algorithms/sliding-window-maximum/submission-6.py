class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for l in range(len(nums)-k+1):
            output.append(max(nums[l:l+k]))
        return output