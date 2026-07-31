class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (r + l)//2
        while l <= r:
            nmid = nums[mid]
            if nmid == target:
                return mid
            elif target < nmid:
                r = mid - 1
            else:
                l = mid + 1
            mid = (r + l)//2
        return -1