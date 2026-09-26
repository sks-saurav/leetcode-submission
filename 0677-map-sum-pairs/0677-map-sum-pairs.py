from collections import defaultdict

class Trie:
    def __init__(self):
        self.child = {}
        self.val = 0

class MapSum:
    def __init__(self):
        self.root = Trie()
        self.dict = defaultdict(int)

    def _get(self, prefix, node):
        for ch in prefix:
            if ch not in node.child:
                return 0
            node = node.child[ch]
        return node.val

    def _add(self, key, val, node):
        delta = val-self.dict[key]
        for ch in key:
            if ch not in node.child:
                node.child[ch] = Trie()
            node = node.child[ch]
            node.val += delta

        self.dict[key] = val

    def insert(self, key: str, val: int) -> None:
        self._add(key, val, self.root)

    def sum(self, prefix: str) -> int:
        return self._get(prefix, self.root)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)