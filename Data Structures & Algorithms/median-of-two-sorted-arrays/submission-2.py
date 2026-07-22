class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []

        i = 0
        j = 0

        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        
        while i<len(nums1):
            nums3.append(nums1[i])
            i += 1
        
        while j<len(nums2):
            nums3.append(nums2[j])
            j += 1
        
        mid = len(nums3)//2

        if len(nums3)%2==0:
            return (nums3[mid] + nums3[mid-1])/2
        else:
            return nums3[mid]