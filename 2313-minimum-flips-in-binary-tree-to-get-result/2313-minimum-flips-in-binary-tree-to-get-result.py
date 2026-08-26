# PREMIUM

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        def dfs(node):
            # Returns a tuple: (min_flips_for_false, min_flips_for_true)
            if node.val == 0:
                return (0, 1)
            elif node.val == 1:
                return (1, 0)
                
            # NOT operation (5)
            if node.val == 5:
                child = node.left if node.left else node.right
                child_F, child_T = dfs(child)
                return (child_T, child_F)

            # Operations requiring both children (OR, AND, XOR)
            left_F, left_T = dfs(node.left)
            right_F, right_T = dfs(node.right)

            if node.val == 2:  # OR
                cost_F = left_F + right_F
                cost_T = min(left_T + right_T, left_T + right_F, left_F + right_T)
                return (cost_F, cost_T)

            elif node.val == 3:  # AND
                cost_F = min(left_F + right_F, left_T + right_F, left_F + right_T)
                cost_T = left_T + right_T
                return (cost_F, cost_T)

            elif node.val == 4:  # XOR
                cost_F = min(left_F + right_F, left_T + right_T)
                cost_T = min(left_F + right_T, left_T + right_F)
                return (cost_F, cost_T)

        cost_false, cost_true = dfs(root)
        return cost_true if result else cost_false
            

            