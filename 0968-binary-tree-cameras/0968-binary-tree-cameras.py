# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        '''
        postorder traversal: (children are prosecced first)
        If a node has children that are not covered by a camera, then we must place a camera here. Additionally, 
        if a node has no parent and it is not covered, we must place a camera here.
        '''

        covered = set([None])
        self.ans = 0

        def dfs(node, parent):
            if node is None:
                return

            dfs(node.left, node)
            dfs(node.right, node)

            if (parent is None and node not in covered) or (node.left not in covered) or (node.right not in covered):
                self.ans += 1
                
                covered.add(node)
                covered.add(parent)

                covered.add(node.left)
                covered.add(node.right)


        dfs(root, None)
        return self.ans
