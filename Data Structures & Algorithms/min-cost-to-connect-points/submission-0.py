class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = {i:[] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y2 - y1)
                adjList[i].append([cost, j])
                adjList[j].append([cost, i])
        
        visit = set()
        res = 0
        minHeap = [[0, 0]]

        while len(visit)<n:
            popCost, popN = heapq.heappop(minHeap)
            if popN in visit:
                continue
            
            res += popCost
            visit.add(popN)

            for nbrCost, nbr in adjList[popN]:
                heapq.heappush(minHeap, (nbrCost, nbr))
        
        return res