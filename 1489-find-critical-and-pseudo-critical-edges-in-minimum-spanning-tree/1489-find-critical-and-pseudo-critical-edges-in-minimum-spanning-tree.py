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

        sorted_edges = sorted([(*edge, i) for i, edge in enumerate(edges)], key=lambda x: x[2])

        def find_mst(parent, ignore_idx=-1, edges_used=0):
            ans = 0
            for u, v, w, orig_idx in sorted_edges:
                if orig_idx == ignore_idx:
                    continue
                    
                if union(u, v, parent):
                    ans += w
                    edges_used += 1
                    
                    if edges_used == n - 1:
                        break
            
            if edges_used != n - 1:
                return float('inf')
                
            return ans

        critical_edges = []
        pseudo_critical_edges = []
        
        base_parent = [i for i in range(n)]
        mst_wt = find_mst(base_parent)

        for i, (u, v, w) in enumerate(edges):
            parent = [j for j in range(n)]
            if find_mst(parent, ignore_idx=i) > mst_wt:
                critical_edges.append(i)
            else:
                parent = [j for j in range(n)]
                union(u, v, parent)
                
                forced_mst_wt = w + find_mst(parent, ignore_idx=i, edges_used=1)
                
                if forced_mst_wt == mst_wt:
                    pseudo_critical_edges.append(i)
        
        return [critical_edges, pseudo_critical_edges]