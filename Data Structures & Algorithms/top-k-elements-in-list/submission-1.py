class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 0
            else:
                freq_dict[i] += 1
        
        tmp_freq_sort = []
        
        for key in freq_dict:
            tmp_freq_sort.append([freq_dict[key], key])
        tmp_freq_sort.sort(reverse=True)

        # print(freq_dict)
        # print(tmp_freq_sort)

        output = []

        for j in range(k):
            output.append(tmp_freq_sort[j][1])
        
        return output