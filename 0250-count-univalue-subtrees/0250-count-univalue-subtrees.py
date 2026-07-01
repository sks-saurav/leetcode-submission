# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def count(node):
            if node is None:
                return (0, set())

            curr_ele_set = set()
            curr_ele_set.add(node.val)

            l, ls = count(node.left)
            r, rs = count(node.right)

            curr_ele_set.update(ls)
            curr_ele_set.update(rs)

            ans = l+r
            if len(curr_ele_set) == 1:
                ans += 1

            return (ans, curr_ele_set)
        
        ans, aset = count(root)
        return ans