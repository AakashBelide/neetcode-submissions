class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}

        for c1, c2 in prerequisites:
            if c1 in adjList:
                adjList[c1].append(c2)
            else:
                adjList[c1] = [c2]
            
            if c2 not in adjList:
                adjList[c2] = []
        
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            
            visit.add(course)

            for nbr in adjList[course]:
                if not dfs(nbr):
                    return False
            
            adjList[course] = []
            visit.remove(course)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True