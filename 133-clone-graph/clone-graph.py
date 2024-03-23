from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        clone_dict = {}
        def dfs(original_node):
            if original_node.val in clone_dict:
                return clone_dict[original_node.val]
            clone = Node(original_node.val)
            clone_dict[original_node.val] = clone
            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)
                    