# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.DELIMITER = '|'

    def serialize(self, root):
        if root is None: return ''

        ans = []
        q = deque([root])

        while q:
            curr = q.popleft()
            if curr:
                ans.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                ans.append('#')

        return self.DELIMITER.join(ans)
        

    def deserialize(self, data):
        if len(data) == 0: return None

        arr = data.split(self.DELIMITER)
        idx = 0

        ans = TreeNode(int(arr[idx]))
        idx += 1
        q = deque([ans])

        while q:
            sz = len(q)
            for _ in range(sz):
                curr = q.popleft()

                if idx < len(arr):
                    l = arr[idx]
                    idx += 1
                    if l != '#':
                        node = TreeNode(int(l))
                        curr.left = node
                        q.append(node)

                if idx < len(arr):
                    r = arr[idx]
                    idx += 1
                    if r != '#':
                        node = TreeNode(int(r))
                        curr.right = node
                        q.append(node)

        return ans


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))