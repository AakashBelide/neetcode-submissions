class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            tmp_set = set()
            for row_val in row:
                if row_val == ".":
                    continue
                elif row_val in tmp_set:
                    return False
                else:
                    tmp_set.add(row_val)
        
        # Check cols
        for i in range(9):
            tmp_set = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in tmp_set:
                    return False
                else:
                    tmp_set.add(board[j][i])
        
        # Check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                tmp_set = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] == ".":
                            continue
                        elif board[k][l] in tmp_set:
                            return False
                        else:
                            tmp_set.add(board[k][l])
                
        return True