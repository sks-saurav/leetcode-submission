class Trie:
    def __init__(self):
        self.child = {}
        self.end = None

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()

        for word in words:
            node = root
            for w in word:
                if not w in node.child:
                    node.child[w] = Trie()
                node = node.child[w]
            node.end = word

        self.ans = ""

        def dfs(node):
            if node.end is None:
               return 
                
            if len(self.ans) < len(node.end):
                self.ans = node.end
            if len(self.ans) == len(node.end) and node.end < self.ans:
                self.ans = node.end

            for ch in node.child:
                dfs(node.child[ch])

        for ch in root.child:
            dfs(root.child[ch])

        return self.ans
                

        