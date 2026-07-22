class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occurence = set()
        visited = set()

        for num in nums:
            occurence.add(num)
        
        output = 0

        for num in nums:
            if num not in visited:
                seq_size = 1
                visited.add(num)
                visit = num
                # print("num:", num)
                while visit+1 in occurence:
                    # print(visit)
                    seq_size += 1
                    visited.add(visit+1)
                    visit += 1
                output = max(output, seq_size)
        
        return output