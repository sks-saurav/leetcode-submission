# PREMIUM

class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # LOG is the maximum power of 2 we need to jump. 
        # For N=1000, 2^10 = 1024, so 10 is enough. We use 11 to be safe.
        LOG = 11 
        up = [[-1] * LOG for _ in range(n)]
        depth = [0] * n
        
        # 1. BFS to compute depths and immediate parents (up[i][0])
        queue = deque([0])
        visited = {0}
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    depth[neighbor] = depth[curr] + 1
                    up[neighbor][0] = curr  # The 2^0 (1st) ancestor is the immediate parent
                    queue.append(neighbor)
                    
        # 2. Binary Lifting Precomputation
        # Fill the table: the 2^j ancestor is the 2^(j-1) ancestor of the 2^(j-1) ancestor
        for j in range(1, LOG):
            for i in range(n):
                if up[i][j-1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]
                    
        # 3. Fast LCA function using Binary Lifting
        def get_lca(u, v):
            # Ensure u is the deeper node
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Jump u up to the same depth as v
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            # Jump both u and v up together, stopping right before they meet
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            # Their immediate parent is the LCA
            return up[u][0]
            
        # 4. Process queries using the Tree Median trick
        final_ans = []
        for start, end, node in query:
            lca1 = get_lca(start, end)
            lca2 = get_lca(start, node)
            lca3 = get_lca(end, node)
            
            # The answer is the LCA that is deepest in the tree
            closest = lca1
            if depth[lca2] > depth[closest]:
                closest = lca2
            if depth[lca3] > depth[closest]:
                closest = lca3
                
            final_ans.append(closest)
            
        return final_ans