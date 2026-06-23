from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))

        visited = [False] * n

        def dfs(u):
            visited[u] = True
            count = 0

            for v, w in adj[u]:
                if not visited[v]:
                    count += w
                    count += dfs(v)

            return count

        return dfs(0)

