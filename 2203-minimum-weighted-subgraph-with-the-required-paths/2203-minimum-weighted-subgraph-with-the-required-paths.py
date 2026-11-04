class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
        adj = defaultdict(list)
        radj = defaultdict(list)

        for u, v, weight in edges:
            adj[u].append((v, weight))
            radj[v].append((u, weight))

        def minDistDijkstra(src, curr_adj):
            que = [(0, src)]
            dist = [float('inf')] * n
            dist[src] = 0

            while que:
                curr_dist, curr_node = heappop(que)

                # Skip stale heap entries (prevents TLE)
                if curr_dist > dist[curr_node]:
                    continue

                for nb_node, weight in curr_adj[curr_node]:

                    if dist[nb_node] > curr_dist + weight:
                        dist[nb_node] = curr_dist + weight
                        heappush(que, (curr_dist+weight, nb_node))

            return dist

        
        dist1 = minDistDijkstra(src1, adj)
        dist2 = minDistDijkstra(src2, adj)
        distd = minDistDijkstra(dest, radj)

        ans = float('inf')

        for meetNode in range(n):
            curr_dist = dist1[meetNode] + dist2[meetNode] + distd[meetNode]
            ans = min(ans, curr_dist)

        return ans if ans != float('inf') else -1