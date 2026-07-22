class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)

        for u, v, t in times:
            adjList[u].append((v, t))
        
        minHeap = [(0, k)]
        visit = set()

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            if len(visit)==n:
                return t1

            for n2, t2 in adjList[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (t1 + t2, n2))
        
        return -1