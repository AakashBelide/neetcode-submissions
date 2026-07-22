class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        for i in range(1, len(nums)-1):
            j = 0
            k = len(nums)-1
            target = -nums[i]
            while j < i and k > i:
                curr_sum = nums[j] + nums[k]
                if curr_sum < target:
                    j += 1
                elif curr_sum > target:
                    k -= 1
                else:
                    output.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
        
        return list(output)