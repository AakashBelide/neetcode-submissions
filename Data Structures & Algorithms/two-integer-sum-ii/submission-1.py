class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i<j:
            tmp_target = numbers[i] + numbers[j]
            if tmp_target > target:
                j -= 1
            elif tmp_target < target:
                i += 1
            else:
                return [i+1, j+1]