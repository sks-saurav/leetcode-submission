# PREMIUM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def path(node):
            if node is None:
                return 0

            curr_len = 1
            pl = path(node.left)
            pr = path(node.right)

            if node.left and node.left.val == node.val + 1:
                curr_len = max(curr_len, 1 + pl)
            if node.right and node.right.val == node.val + 1:
                curr_len = max(curr_len, 1 + pr)
            self.ans = max(self.ans, curr_len)

            return curr_len

        path(root)
        return self.ans
