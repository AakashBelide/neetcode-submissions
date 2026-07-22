class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2

        if len(B) < len(A):
            A, B = B, A
        
        l = 0
        r = len(A) - 1

        while True:
            a_mid = (l + r)//2
            b_mid = half - a_mid - 2

            A_left = A[a_mid] if a_mid >=0 else float("-infinity")
            A_right = A[a_mid + 1] if (a_mid + 1) < len(A) else float("infinity")
            B_left = B[b_mid] if b_mid >=0 else float("-infinity")
            B_right = B[b_mid + 1] if (b_mid + 1) < len(B) else float("infinity")

            if A_left <= B_right and B_left <= A_right:
                if total%2:
                    return min(A_right, B_right)
                return (max(A_left, B_left) + min(A_right, B_right))/2
            elif A_left > B_right:
                r = a_mid - 1
            else:
                l = a_mid + 1
            