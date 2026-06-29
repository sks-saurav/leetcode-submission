# PREMIUM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        candidate = set(tree)

        for node in tree:
            for child_node in node.children:
                if child_node in candidate:
                    candidate.remove(child_node)

        if len(candidate) == 1:
            return list(candidate)[0]
        return None