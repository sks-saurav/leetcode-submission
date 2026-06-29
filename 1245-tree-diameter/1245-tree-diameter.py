# PREMIUM

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        ans = 0
        def dfs(u, parent):
            nonlocal ans
            curr_path_len = [0]

            for v in adj[u]:
                if v == parent: continue
                path_len = dfs(v, u) + 1
                curr_path_len.append(path_len)

            if len(curr_path_len) == 1:
                return 0

            curr_path_len.sort(reverse=True)
            ans = max(ans, curr_path_len[0] + curr_path_len[1])
            
            return curr_path_len[0]

        dfs(0, -1)
        return ans
