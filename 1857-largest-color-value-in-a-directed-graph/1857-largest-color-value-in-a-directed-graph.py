class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = defaultdict(set)
        indeg = [0] * n
        color_dict = {i : [0] * 26 for i in range(n)}
        color_vals = [ord(c) - 97 for c in colors]

        for a, b in edges:
            adj[a].add(b)
            indeg[b] += 1

        que = deque()
        for i in range(n):
            if indeg[i] == 0:
                que.append(i)

        ans = 0
        visited = 0
        while que:
            curr = que.popleft()
            c_val = color_vals[curr]
            color_dict[curr][c_val] += 1

            ans = max(ans,  color_dict[curr][c_val])
            visited += 1

            for nxt in adj[curr]:
                for i in range(26):
                    color_dict[nxt][i] = max(color_dict[nxt][i], color_dict[curr][i])

                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    que.append(nxt)

        return ans if visited == n else -1
        
        

        


