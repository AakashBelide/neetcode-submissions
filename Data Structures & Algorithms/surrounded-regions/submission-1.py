class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs (r, c):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]=='T' or board[r][c]=='X':
                return
            
            board[r][c] = 'T'

            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                dfs(new_r, new_c)
            
            return
        
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1 and board[r][c]=="O"):
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"