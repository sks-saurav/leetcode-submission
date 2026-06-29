# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        visited = set()
        def remove_invalid(node, parent, lr):
            if node is None:
                return
            visited.add(node)
            
            if node.right in visited:
                if lr == 0:
                    parent.left = None
                else:
                    parent.right = None
                return
                
            remove_invalid(node.right, node, 1)
            remove_invalid(node.left, node, 0)

        remove_invalid(root, None, -1)
        return root