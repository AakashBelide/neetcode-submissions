class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        total = n*m

        def getPos(num):
            c = num%m
            r = num//m
            return r, c
        
        left = 0
        right = total - 1

        while left<=right:
            mid = left + (right - left)//2
            r, c = getPos(mid)
            if matrix[r][c] > target:
                right = mid - 1
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                return True

        return False