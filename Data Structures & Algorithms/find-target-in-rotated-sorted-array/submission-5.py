class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l
        
        def binarySearch(left, right, t):
            while left<=right:
                mid = (left + right)//2

                if t < nums[mid]:
                    right = mid - 1
                elif t > nums[mid]:
                    left = mid + 1
                else:
                    return mid
            return -1
        
        if target >= nums[pivot] and target <= nums[-1]:
            return binarySearch(pivot, len(nums)-1, target)
        else:
            return binarySearch(0, pivot-1, target)