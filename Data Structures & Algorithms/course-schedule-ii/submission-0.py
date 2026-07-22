class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}

        for c1, c2 in prerequisites:
            adjList[c1].append(c2)

        visit, cycle = set(), set()

        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)
            for nbr in adjList[crs]:
                if not dfs(nbr):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output