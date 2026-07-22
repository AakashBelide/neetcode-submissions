class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp_dict = {}
        for i in nums:
            if i not in tmp_dict:
                tmp_dict[i] = 1
            else:
                return True
        return False