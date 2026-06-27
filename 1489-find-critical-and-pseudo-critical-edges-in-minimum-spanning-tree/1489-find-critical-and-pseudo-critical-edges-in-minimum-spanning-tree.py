class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def get_parent(u, parent):
            if parent[u] != u:
                parent[u] = get_parent(parent[u], parent)
            return parent[u]

        def union(u, v, parent):
            pu = get_parent(u, parent)
            pv = get_parent(v, parent)
            if pu != pv:
                parent[pu] = pv
                return True
            return False

        def find_mst(parent, ignore_idx=-1, edges_used=0):
            heap = []
            for j in range(len(edges)):
                if j == ignore_idx:
                    continue
                heappush(heap, (edges[j][2], edges[j][0], edges[j][1]))

            ans = 0
            while heap:
                wt, a, b = heappop(heap)
                if union(a, b, parent):
                    ans += wt
                    edges_used += 1
            
            if edges_used != n - 1:
                return float('inf')
                
            return ans

        critical_edge = set()
        p_critical_edge = []
        mst_wt = find_mst([j for j in range(n)])

        # critical
        for i in range(len(edges)):
            parent = [j for j in range(n)]
            t_mst_wt = find_mst(parent, ignore_idx = i)
            if t_mst_wt > mst_wt:
                critical_edge.add(i)

        #pseudo critical
        for i in range(len(edges)):
            if i in critical_edge:
                continue
            parent = [j for j in range(n)]
            union(edges[i][0], edges[i][1], parent)
            t_mst_wt = edges[i][2] + find_mst(parent, ignore_idx=i, edges_used=1)
            if t_mst_wt == mst_wt:
                p_critical_edge.append(i)
        
        return [list(critical_edge), p_critical_edge]
