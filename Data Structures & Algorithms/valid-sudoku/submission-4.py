class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            tmp_set_i = set()
            tmp_set_j = set()
            for j in range(9):
                element_i = board[i][j]
                if element_i!="." and element_i not in tmp_set_i:
                    tmp_set_i.add(element_i)
                elif element_i in tmp_set_i:
                    return False
                element_j = board[j][i]
                if element_j!="." and element_j not in tmp_set_j:
                    tmp_set_j.add(element_j)
                elif element_j in tmp_set_j:
                    return False
        
        for i in range(9):
            tmp_set_k = set()
            for j in range(3):
                for k in range(3):
                    row = (i//3)*3 + j
                    col = (i%3)*3 + k
                    element = board[row][col]
                    if element!="." and element not in tmp_set_k:
                        tmp_set_k.add(element)
                    elif element in tmp_set_k:
                        return False

        return True