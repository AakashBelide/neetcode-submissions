class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        
        left_ptr = 1
        for i in range(n):
            output[i] = left_ptr
            left_ptr *= nums[i]
        
        right_ptr = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_ptr
            right_ptr *= nums[i]
        
        return output