# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = float(inf)
        ans = -1

        def traverse(node):
            if node is None:
                return 

            nonlocal diff
            nonlocal ans

            c_diff = abs(target - node.val)
            if c_diff < diff:
                diff = c_diff
                ans = node.val
            if c_diff == diff:
                ans = min(ans, node.val)

            if target < node.val:
                traverse(node.left)
            else:
                traverse(node.right)

        
        traverse(root)
        return ans