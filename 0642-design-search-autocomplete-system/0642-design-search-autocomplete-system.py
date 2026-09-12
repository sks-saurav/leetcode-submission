class Trie:
    def __init__(self):
        self.child = {}
        self.eligible = []

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.hotness = defaultdict(int)
        self.root = Trie()
        self._build(sentences, times)
        self.curr_node = self.root
        self.curr_word = ""

    def _build(self, sentences, times):
        for i in range(len(sentences)):
            self._add_trie(sentences[i])
            self.hotness[sentences[i]] = times[i]
        
    def _add_trie(self, sentence):
        node = self.root
        for i in range(len(sentence)):
            ch = sentence[i]
            if ch not in node.child:
                node.child[ch] = Trie()
            node = node.child[ch]
            node.eligible.append(sentence)

    def input(self, c: str) -> List[str]:
        if c == '#':
            if self.curr_word not in self.hotness:
                self._add_trie(self.curr_word)

            self.hotness[self.curr_word] += 1
            self.curr_node = self.root
            self.curr_word = ""
            return []

        self.curr_word += c

        if self.curr_node is not None:
            self.curr_node = self.curr_node.child.get(c, None)

        res = []
        if self.curr_node is None:
            return res

        t_data = [(-self.hotness[w], w) for w in self.curr_node.eligible]
        t_data.sort()

        for _, sentence in t_data[:3]:
            res.append(sentence)

        return res

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)