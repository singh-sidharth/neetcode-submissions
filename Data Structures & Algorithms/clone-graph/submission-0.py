"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}
        # store clones
        def dfs(node: Optional['Node']):
            if node in oldToNew:
                return oldToNew[node]
            # make clone and store
            copy = Node(node.val)
            oldToNew[node] = copy
            # loop through neightbors to clone  
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        # Use adjacency list to create clone
        return dfs(node) if node else None
