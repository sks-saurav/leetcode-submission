# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        
        def traverse(node):
            if node is None:
                return ""

            if node.len == 0:
                return node.val

            return traverse(node.left) + traverse(node.right)

        return traverse(root)[k-1]
