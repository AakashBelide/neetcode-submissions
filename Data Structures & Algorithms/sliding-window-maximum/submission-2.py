class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        tmp_max = -9999999
        for i in range(k):
            if nums[i]>tmp_max:
                tmp_max = nums[i]
        
        output.append(tmp_max)
        l = 0
        r = k
        # print(nums[l:r], output)
        # print("Start")
        while r < len(nums):
            # print(nums[l:r], "; l:", l, "; r:", r, ";", nums[l], nums[r], output[-1], nums[l]!=output[-1] and nums[r]<output[-1])
            # print(nums[l:r], output)
            if nums[r]>=output[-1]:
                # print("A")
                output.append(nums[r])
            elif nums[l]==output[-1] and nums[r]<nums[l]:
                # print("B")
                tmp_max = -9999999
                for i in range(l+1, r+1):
                    if nums[i]>tmp_max:
                        tmp_max = nums[i]
                output.append(tmp_max)
            elif nums[l]!=output[-1] and nums[r]<output[-1]:
                # print("C")
                output.append(output[-1])
            l += 1
            r += 1
        return output