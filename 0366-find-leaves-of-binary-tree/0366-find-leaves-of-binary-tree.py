# PREMIUM

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ht_dict = defaultdict(list)
        
        def calc_height(node):
            if node is None:
                return -1

            lh = calc_height(node.left)
            rh = calc_height(node.right)

            ht = 1 + max(lh, rh)
            ht_dict[ht].append(node.val)

            return ht

        calc_height(root)
        ans = []
        for i in range(max(ht_dict.keys())+1):
            if i in ht_dict:
                ans.append(ht_dict[i])

        return ans

