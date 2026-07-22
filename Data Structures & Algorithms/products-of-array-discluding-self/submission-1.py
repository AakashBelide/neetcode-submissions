class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [0]*len(nums)

        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            left.append(prod)
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            right[i] = prod

        output = []

        for i in range(len(left)):
            if i == 0:
                output.append(right[i+1])
            elif i == len(left)-1:
                output.append(left[i-1])
            else:
                output.append(left[i-1]*right[i+1])

        return output