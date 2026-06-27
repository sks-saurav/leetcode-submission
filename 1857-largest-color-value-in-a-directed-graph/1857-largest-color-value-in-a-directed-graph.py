class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = defaultdict(set)
        indeg = [0] * n
        color_dict = {i : [0] * 26 for i in range(n)}

        for a, b in edges:
            adj[a].add(b)
            indeg[b] += 1

        que = deque()
        for i in range(n):
            if indeg[i] == 0:
                que.append(i)

        ans = 0
        order = []
        while que:
            curr = que.popleft()
            c_val = ord(colors[curr]) - ord('a')
            color_dict[curr][c_val] += 1

            ans = max(ans,  color_dict[curr][c_val])
            order.append(curr)

            for nxt in adj[curr]:
                for i in range(26):
                    color_dict[nxt][i] = max(color_dict[nxt][i], color_dict[curr][i])

                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    que.append(nxt)

        return ans if len(order) == len(indeg) else -1
        
        

        


