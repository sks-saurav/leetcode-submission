#PREMIUM
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]

        def get_parent(u):
            if parent[u] != u:
                parent[u] = get_parent(parent[u])
            return parent[u]

        def union(u, v):
            pu = get_parent(u)
            pv = get_parent(v)
            if pu != pv:
                parent[pu] = pv
                return True
            return False

        heap = []
        for u, v, cost in pipes:
            heappush(heap, (cost, u, v))

        for u in range(1, n+1):
            heappush(heap, (wells[u-1], 0, u))

        ans = 0
        while heap:
            cost, u, v = heappop(heap)
            if union(u, v):
                ans += cost

        return ans

            