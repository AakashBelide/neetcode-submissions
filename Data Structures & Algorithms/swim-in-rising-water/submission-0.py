class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]
        visit.add((0, 0))
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while True:
            popH, popR, popC = heapq.heappop(minHeap)

            if popR == n-1 and popC == n-1:
                return popH

            for dr, dc in dirs:
                new_r, new_c = popR + dr, popC + dc
                if new_r<0 or new_c<0 or new_r>=n or new_c>=n or (new_r, new_c) in visit:
                    continue
                visit.add((new_r, new_c))
                heapq.heappush(minHeap, [max(popH, grid[new_r][new_c]), new_r, new_c])