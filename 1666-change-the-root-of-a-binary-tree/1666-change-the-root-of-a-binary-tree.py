# PREMIUM
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        if root is None or leaf is None:
            return root

        curr = leaf
        new_parent = None 
        
        while curr != root:
            curr_p = curr.parent
            if curr == curr_p.left:
                curr_p.left = None
            else:
                curr_p.right = None
            if curr.left:
                curr.right = curr.left
                
            curr.left = curr_p
            curr.parent = new_parent

            new_parent = curr
            curr = curr_p

        curr.parent = new_parent

        return leaf