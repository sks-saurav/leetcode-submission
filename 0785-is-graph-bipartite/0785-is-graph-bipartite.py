class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        node_color = [2] * n

        def dfs(u, curr_col):
            node_color[u] = curr_col
            
            for v in graph[u]:
                if node_color[v] == node_color[u]:
                    return False
                if node_color[v] == 2:
                    if not dfs(v, 1-curr_col):
                        return False
            return True
        
        ans = True
        for i in range(n):
            if node_color[i] == 2:
                ans = ans and dfs(i, 0)

        return ans

            