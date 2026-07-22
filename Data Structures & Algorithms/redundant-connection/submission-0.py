class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]

        def find(node):
            par = parent[node]

            while par!=parent[par]:
                parent[par] = parent[parent[par]]
                par = parent[par]
            
            return par
        
        def union(a, b):
            p1, p2 = find(a), find(b)

            if p1==p2:
                return False
            
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]