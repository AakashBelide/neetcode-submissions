class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for i in range(len(nums)-k+1):
            tmp_max = -9999999
            for j in range(i, i+k):
                if nums[j]>tmp_max:
                    tmp_max = nums[j]
            output.append(tmp_max)
        return output