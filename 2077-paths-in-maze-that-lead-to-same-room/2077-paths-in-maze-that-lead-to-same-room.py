from typing import List

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        degree = [0] * (n + 1)
        for u, v in corridors:
            degree[u] += 1
            degree[v] += 1
            
        adj = defaultdict(set)
        for u, v in corridors:
            if degree[u] < degree[v] or (degree[u] == degree[v] and u < v):
                adj[u].add(v)
            else:
                adj[v].add(u)
                
        ans = 0
        for u in range(1, n + 1):
            for v in adj[u]:
                ans += len(adj[u] & adj[v])
                
        return ans