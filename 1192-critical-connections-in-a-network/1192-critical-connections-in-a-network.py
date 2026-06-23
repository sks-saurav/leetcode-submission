class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        critical_v = []
        time = [0 for _ in range(n)]
        low = [0 for _ in range(n)]
        self.curr_time = 0

        def dfs(u, parent):
            self.curr_time += 1
            time[u] = self.curr_time
            low[u] = self.curr_time

            for v in adj[u]:
                if v == parent:
                    continue
                if time[v] == 0: #not visited
                    dfs(v, u)
                    if time[u] < low[v]:
                        critical_v.append([u, v])
                    low[u] = min(low[u], low[v])
                else: # visited
                    low[u] = min(low[u], low[v])

        dfs(0, -1)
        return critical_v
