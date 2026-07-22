class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)-1):
            j = i+1
            k = len(nums)-1
            target = -nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j < k:
                curr_sum = nums[j] + nums[k]
                if curr_sum < target:
                    j += 1
                elif curr_sum > target:
                    k -= 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j]==nums[j-1] and j<k:
                        j += 1
        
        return output