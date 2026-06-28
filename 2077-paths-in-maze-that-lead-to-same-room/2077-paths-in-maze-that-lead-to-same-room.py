class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        adj = defaultdict(set)
        
        for u, v in corridors:
            adj[u].add(v)
            adj[v].add(u)

        ans = 0
        for u, v in corridors:
            # Common neighbors of u and v form a cycle of length 3
            ans += len(adj[u] & adj[v])
            
        return ans // 3