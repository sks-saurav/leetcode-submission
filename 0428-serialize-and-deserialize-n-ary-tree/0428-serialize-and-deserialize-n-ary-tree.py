"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def __init__(self):
        self.next_id = 0

    def _get_next_id(self):
        self.next_id += 1
        return self.next_id
    
    def _get_node_id(self, node, node_id_dict):
        if node not in node_id_dict:
            node_id_dict[node] = self._get_next_id()
        return node_id_dict[node]

    def _serialize_helper(self, node, node_id_dict):
        if node is None:
            return ""

        nid = self._get_node_id(node, node_id_dict)

        ans = []
        ans.append(nid)
        ans.append(node.val)
        ans.append(len(node.children))
        for child in node.children:
            ans.append(self._get_node_id(child, node_id_dict))
        
        ans ="|".join(map(str, ans))
        for child in node.children:
            ans += '|'
            ans += self._serialize_helper(child, node_id_dict)
        return ans


    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        ans = self._serialize_helper(root, {})
        return ans
    
    def _get_node(self, nid, node_dict):
        if nid not in node_dict:
            node_dict[nid] = Node()
        return node_dict[nid]
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data or len(data) == 0:
            return None
        root = None
        node_dict = {}
        i = 0
        data_arr = [int(x) for x in data.split("|")]
        while i < len(data_arr):
            nid = data_arr[i]
            val = data_arr[i+1]
            child_count = data_arr[i+2]

            node = self._get_node(nid, node_dict)
            if i == 0:
                root = node

            node.val = val
            i += 3
            for _ in range(child_count):
                ch_id = data_arr[i]
                i += 1
                node.children.append(self._get_node(ch_id, node_dict))

        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))