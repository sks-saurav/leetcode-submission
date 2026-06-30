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
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # if node has right child -> successor present in rhs
        # else successor is above in parent
        successor = None
        target_val = node.val

        def get_successor_above(node):
            nonlocal successor

            while node:
                if node.val > target_val:
                    successor = node
                    break
                
                node = node.parent


        def get_successor_below(node):
            nonlocal successor

            if not node:
                return

            if node.val > target_val:
                successor = node
                get_successor_below(node.left)
            else:
                get_successor_below(node.right)


        if node.right:
            get_successor_below(node.right)
        else:
            get_successor_above(node.parent)

        return  successor