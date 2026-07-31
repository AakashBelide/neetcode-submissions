class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = 0, (row*col) -1
        mid = (r+l)//2

        while l<=r:
            nrow, ncol = mid//col, mid%col
            nmid = matrix[nrow][ncol]
            if nmid == target:
                return True
            elif target<nmid:
                r = mid-1
            else:
                l = mid+1
            mid = (r+l)//2
        
        return False