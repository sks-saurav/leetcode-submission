class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
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

        def is_equiv(a, b):
            if len(a) != len(b):
                return False

            swap = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    swap += 1
            
            return swap == 0  or swap == 2


        for i in range(n):
            for j in range(i+1, n):
                eq = is_equiv(strs[i], strs[j])
                if eq:
                    union(i, j)

        unique_grp = set()
        for i in range(n):
            unique_grp.add(get_parent(i))

        return len(unique_grp)