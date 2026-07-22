"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        graphMap = {}

        def dfs(currNode):
            newNode = Node()
            if currNode:
                if currNode not in graphMap:
                    newNode.val = currNode.val
                    graphMap[currNode] = newNode
                else:
                    return graphMap[currNode]
            
                for nbr in currNode.neighbors:
                    newNode.neighbors.append(dfs(nbr))
            return newNode
        
        return dfs(node)



