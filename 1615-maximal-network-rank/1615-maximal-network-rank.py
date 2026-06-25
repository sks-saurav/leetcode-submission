class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxRank = 0
        adj = defaultdict(set)
        for u, v in roads:
            adj[u].add(v)
            adj[v].add(u)

        for i in range(n):
            for j in range(i + 1, n):
                currentRank = len(adj[i]) + len(adj[j])
                if i in adj[j]:
                    currentRank -= 1
                maxRank = max(maxRank, currentRank)

        return maxRank    