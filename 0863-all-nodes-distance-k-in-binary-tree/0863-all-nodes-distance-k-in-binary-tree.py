# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None or target is None:
            return []

        parent = {}

        def tree_traverse(node, p):
            if node is None:
                return
            parent[node] = p

            tree_traverse(node.left, node)
            tree_traverse(node.right, node)

        tree_traverse(root, None)
        que = deque([(target, 0)])
        seen = set()
        seen.add(target)
        ans = []

        while que:
            node, step = que.popleft()
            if step == k:
                ans.append(node.val)
                continue

            pp = None
            if node in parent:
                pp = parent[node]

            for next_node in (node.left, node.right, pp):
                if next_node is not None and next_node not in seen:
                    seen.add(next_node)
                    que.append((next_node, step+1))
        
        return ans