# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        preorder = []
        def trav(node):
            if node is None:
                return

            trav(node.left)
            preorder.append(node.val)
            trav(node.right)


        trav(root)
        idx = bisect_left(preorder, target)
        ans = []
        l, r = idx-1, idx

        while len(ans) < k:
            if r == len(preorder) or abs(preorder[l]-target) < abs(preorder[r]-target):
                ans.append(preorder[l])
                l -= 1
            else:
                ans.append(preorder[r])
                r += 1

        return ans
