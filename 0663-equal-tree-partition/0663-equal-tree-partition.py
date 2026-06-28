# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        tree_sum = defaultdict(int)
        tree_sum[None] = 0

        def cal_sum(node):
            if node is None:
                return 0
            curr_sum = cal_sum(node.left) + cal_sum(node.right) + node.val
            tree_sum[node] = curr_sum
            return curr_sum
        
        cal_sum(root)
        if tree_sum[root]%2 != 0:
            return False
        
        half_sum = tree_sum[root]//2

        def find_edge(node):
            if node is None:
                return False
            if node.left is not None and half_sum == tree_sum[node.left]:
                return True
            if node.right is not None and half_sum == tree_sum[node.right]:
                return True
            return find_edge(node.left) or find_edge(node.right)
            
        return find_edge(root)
