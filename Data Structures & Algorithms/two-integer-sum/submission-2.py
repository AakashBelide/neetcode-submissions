class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {}

        visit[nums[0]] = 0

        for i in range(1, len(nums)):
            diff = target - nums[i]

            if diff in visit:
                return [visit[diff], i]
            
            visit[nums[i]] = i