class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indeg = [0] * n
        edges_set = set()

        for u, v in roads:
            indeg[u] += 1
            indeg[v] += 1
            edges_set.add((u, v))
            edges_set.add((v, u))

        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = indeg[i] + indeg[j]
                if (i, j) in edges_set:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank