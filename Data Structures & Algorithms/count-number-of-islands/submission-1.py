from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        output = 0
        visit = set()

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
            
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc]=="1" and ((nr,nc) not in visit)):
                        q.append((nr, nc))
                        visit.add((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c]=="1":
                    bfs(r, c)
                    output += 1
        
        return output





