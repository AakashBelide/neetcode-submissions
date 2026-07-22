class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums))]

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        for key in count:
            freq[count[key]-1].append(key)

        output = []

        for j in range(len(freq)-1, -1, -1):
            for l in range(len(freq[j])):
                output.append(freq[j][l])
                k -= 1
                if k == 0:
                    return output