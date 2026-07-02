# Premium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def dfs(node, arr):
            if not node:
                return
            
            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)
        
        arr = []
        dfs(root, arr)
        
        arr.sort(key = lambda x: (abs(x - target), x))
        return arr[:k]
        