class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        prod = 1
        for i in range(len(nums)-1):
            prod *= nums[i]
            output.append(prod)
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= prod
            prod *= nums[i]

        return output