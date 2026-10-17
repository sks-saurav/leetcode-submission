# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        
        @cache
        def helper(x):
            if x == 1:
                return [TreeNode()]

            if x%2 == 0:
                return []
            
            ans = []
            for k in range(1, x-1):
                if k%2 == 0 or (x-k-1)%2 == 0:
                    continue

                left = helper(k)
                right = helper(x-1-k)

                for l in left:
                    for r in right:
                        node = TreeNode()
                        node.left = l
                        node.right = r
                        ans.append(node) 

            return ans

        return helper(n)


        