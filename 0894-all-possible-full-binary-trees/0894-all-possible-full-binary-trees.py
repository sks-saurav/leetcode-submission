# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        if n%2 == 0:
            return []

        dp = [[] for _ in range(n+1)]
        dp[1] = [TreeNode()]

        for count in range(3, n+1, 2):
            for lc in range(1, count-1):
                rc = count - 1 - lc
                for lnode in dp[lc]:
                    for rnode in dp[rc]:
                        node = TreeNode()
                        node.left = lnode
                        node.right = rnode
                        dp[count].append(node)

        return dp[n]