class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occurence = set()

        for num in nums:
            occurence.add(num)
        
        output = 0

        for num in nums:
            if num-1 not in occurence:
                seq_size = 1
                while num+seq_size in occurence:
                    seq_size += 1
                output = max(output, seq_size)
        
        return output