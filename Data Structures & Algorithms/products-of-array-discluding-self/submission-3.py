class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        n = len(nums)
        right = [0]*n
        
        left_ptr = 1
        for i in range(n):
            left_ptr *= nums[i]
            left.append(left_ptr)
        
        right_ptr = 1
        for i in range(n-1, -1, -1):
            right_ptr *= nums[i]
            right[i] = right_ptr
        
        output = []
        
        for i in range(n):
            if i==0:
                output.append(right[i+1])
            elif i == n-1:
                output.append(left[i-1])
            else:
                output.append(left[i-1]*right[i+1])
        
        return output