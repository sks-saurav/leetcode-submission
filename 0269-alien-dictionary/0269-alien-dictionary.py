class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indeg = defaultdict(int)

        for word in words:
            for ch in word:
                indeg[ch] = 0

        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        for k in adj:
            for u in adj[k]:
                indeg[u] += 1

        print(indeg)
        print(adj)

        que = deque()
        for k in indeg:
            if indeg[k] == 0:
                que.append(k)

        order = []
        while que:
            curr = que.popleft()
            order.append(curr)
            for nxt in adj[curr]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    que.append(nxt)
        print(order)

        return ''.join(order) if len(order) == len(indeg) else ""

