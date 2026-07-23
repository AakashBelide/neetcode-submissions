class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
        
        buckets = [[] for i in range(len(nums)+1)]

        for key in num_count:
            buckets[num_count[key]].append(key)

        output = []

        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])-1, -1, -1):
                if k >0:
                    output.append(buckets[i][j])
                    k -= 1
                else:
                    return output
        return output
