#PREMIUM

class DistanceLimitedPathsExist:
    def __init__(self, n: int, edgeList: List[List[int]]):
        self.parent = list(range(n))
        self.weight = [0] * n
        
        edgeList.sort(key=lambda x: x[2])
        for u, v, w in edgeList:
            self._union(u, v, w)

    def _find(self, i: int, limit: int = float('inf')) -> int:
        # Traverse up the tree as long as the edge weight is strictly less than the limit
        while i != self.parent[i] and self.weight[i] < limit:
            i = self.parent[i]
        return i

    def _union(self, u: int, v: int, w: int):
        # We don't use path compression here during setup because it destroys 
        # the history of edge weights we need for queries.
        root_u = self._find(u)
        root_v = self._find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v
            self.weight[root_u] = w

    def query(self, p: int, q: int, limit: int) -> bool:
        return self._find(p, limit) == self._find(q, limit)



'''
Here is a high-level blueprint of the DSU with history approach, which is much more efficient:

Initialize: Sort the edgeList by distance in ascending order.

Union-Find Structure: Create a DSU, but modify it so that when you merge two nodes (Union), you record the weight at which they were merged.

Instead of a simple parent array, each node keeps track of the weight that connected it to its parent: self.weight[x] = wt.

Query: To find if p and q are connected under a certain limit, you traverse up the parent pointers for both p and q.

You only move up to a parent if the weight recorded for that connection is strictly less than limit.

If p and q eventually reach the same root using only valid edges, you return True.

'''