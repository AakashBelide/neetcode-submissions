class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visit = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs (r, c):
            if r<0 or c<0 or r>=rows or c>=cols or (r, c) in visit or board[r][c]=='X':
                return
            
            visit.add((r,c))

            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                dfs(new_r, new_c)
            
            return
        
        for r in range(rows):
            for c in range(cols):
                if ((r == 0 or r == rows-1 or c == 0 or c == cols-1 and (r, c) not in visit) and board[r][c]=="O"):
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit:
                    board[r][c] = "X"