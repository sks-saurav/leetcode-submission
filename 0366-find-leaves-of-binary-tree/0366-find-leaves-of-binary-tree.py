# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        parent = {}
        parent[root] = None

        que = deque()
        indeg = defaultdict(int)

        def traverse(node, node_p):
            if node is None:
                return

            parent[node] = node_p
            if node.left is None and node.right is None:
                que.append(node)

            if node.left:
                indeg[node] += 1
                traverse(node.left, node)

            if node.right:
                indeg[node] += 1
                traverse(node.right, node)

        traverse(root, None)
        ans = []
        while que:
            ll = len(que)
            tans = []

            for _ in range(ll):
                curr = que.popleft()
                tans.append(curr.val)
                p_curr = parent[curr]

                if p_curr:
                    indeg[p_curr] -= 1
                    if indeg[p_curr] == 0:
                        que.append(p_curr)

            ans.append(tans)

        return ans