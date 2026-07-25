class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = {}
        nums.sort()
        for i in range(len(nums)):
            target = nums[i]
            l, r = i+1, len(nums)-1
            while l<r:
                curr_sum = nums[l] + nums[r] + target

                if curr_sum == 0:
                    output[f"{nums[i]}_{nums[l]}_{nums[r]}"] = [nums[i], nums[l], nums[r]]
                
                if curr_sum >= 0:
                    r -= 1
                elif curr_sum <= 0:
                    l += 1
                
                
        
        return [output[key] for key in output]