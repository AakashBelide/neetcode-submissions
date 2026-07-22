class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        visit = set()
        
        adjList = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        def dfs(node, prevNode):
            if node in visit:
                return False
            
            visit.add(node)
            
            for nbr in adjList[node]:
                if nbr==prevNode:
                    continue
                if not dfs(nbr, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit)==n