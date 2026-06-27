class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
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
                return True

            return False

        heap = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(heap, (dist, i, j))

        ans = 0
        edge_count = 0
        while heap:
            dist, u, v = heappop(heap)
            if union(u, v):
                edge_count += 1
                ans += dist

            if edge_count == n-1:
                break

        return ans