# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found = set()
        def inorder(node):
            if not node:
                return
            if node.val == p.val or node.val == q.val:
                found.add(node)

            inorder(node.left)
            inorder(node.right)
            

        def helper(node):
            if not node:
                return node
            if node.val == p.val or node.val == q.val:
                return node

            l = helper(node.left)
            r = helper(node.right)

            if l and r:
                return node

            return l if l else r

        inorder(root)
        lca = helper(root)
        return lca if len(found) == 2 else None
        