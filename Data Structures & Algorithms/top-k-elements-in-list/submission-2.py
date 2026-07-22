class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1
        
        tmp_freq_buckets = [[] for i in range(len(nums))]
        
        for key in freq_dict:
            tmp_freq_buckets[freq_dict[key]-1].append(key)

        output = []

        for j in range(len(tmp_freq_buckets)-1,-1,-1):
            for l in range(len(tmp_freq_buckets[j])):
                output.append(tmp_freq_buckets[j][l])
                k -= 1
                if k == 0:
                    return output
        
        return output