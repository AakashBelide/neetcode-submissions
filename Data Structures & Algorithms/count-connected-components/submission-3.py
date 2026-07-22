class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = []
        rank = []

        for i in range(n):
            parent.append(i)
            rank.append(1)
        
        def find(node):
            par = parent[node]

            while par!=parent[par]:
                parent[par] = parent[parent[par]]
                par = parent[par]
            
            return par
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1==p2:
                return 0
            
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return 1

        for n1, n2 in edges:
            n -= union(n1, n2)
        
        return n