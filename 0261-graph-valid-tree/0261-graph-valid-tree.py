'''
Condition:
1. one root / one connected component
2. no cycle
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [False] * n
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def have_cycle(u, parent):
            if visited[u]:
                return True
            
            visited[u] = True
            for v in adj[u]:
                if v == parent:
                    continue
                if have_cycle(v, u):
                    return True
            return False

        if have_cycle(0, -1) or not all(visited):
            return False
        
        return True