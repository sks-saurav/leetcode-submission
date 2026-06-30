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
        def get_l(node):
            if node is None:
                return 0
            if node.len != 0:
                return node.len
            return len(node.val)
        
        def traverse(node, idx):
            if node is None:
                return None

            if node.len == 0:
                return node.val[idx-1]

            ll = get_l(node.left)
            if idx <= ll:
                return traverse(node.left, idx)
            else:
                return traverse(node.right, idx-ll)
            

        return traverse(root, k)
