class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def get_parent(u):
            if parent[u] != u:
                parent[u] = get_parent(parent[u])
            return parent[u]

        def union(u, v):
            pu = get_parent(u)
            pv = get_parent(v)
            if pu != pv:
                parent[pu] = pv

        heap = []
        for a, b, cost in connections:
            heappush(heap, (cost, a-1, b-1))

        ans = 0
        while heap:
            cost, a, b = heappop(heap)

            if get_parent(a) != get_parent(b):
                union(a, b)
                ans += cost

        cluster = set()
        for i in range(n):
            cluster.add(get_parent(i))

        return ans if len(cluster) == 1 else -1
