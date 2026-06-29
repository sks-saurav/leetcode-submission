# PREMIUM

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return root
            
        que = deque([root])

        while que:
            curr_len = len(que)
            for i in range(curr_len):
                if que[i] == u:
                    return que[i+1] if i+1 < curr_len else None

            for i in range(curr_len):
                node = que.popleft()
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)

        return None


