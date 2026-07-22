class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i+1: [] for i in range(n)}
        for u, v, t in times:
            if u not in adjList:
                adjList[u] = []
            adjList[u].append((v, t))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            t = max(t, t1)

            for n2, t2 in adjList[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (t1 + t2, n2))
        
        return t if len(visit)==n else -1