class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)

            for nbr in adjList[node]:
                dfs(nbr)

            return
        
        output = 0

        for i in range(n):
            if i not in visit:
                dfs(i)
                output += 1
        
        return output