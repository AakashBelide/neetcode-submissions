class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kv = {nums[0]: 0}

        for i in range(1, len(nums)):
            find_num = target - nums[i]
            if find_num in kv:
                return [kv[find_num], i]
            else:
                kv[nums[i]] = i