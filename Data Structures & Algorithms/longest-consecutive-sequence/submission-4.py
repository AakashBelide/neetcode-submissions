class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        nums_set = set()

        for i in range(len(nums)):
            if nums[i] not in nums_set:
                nums_set.add(nums[i])

        for i in range(len(nums)):
            seq_len = 1
            if nums[i]-1 not in nums_set:
                tmp_num = nums[i]+1
                while tmp_num in nums_set:
                    seq_len += 1
                    tmp_num += 1
                output = max(output, seq_len)
        
        return output