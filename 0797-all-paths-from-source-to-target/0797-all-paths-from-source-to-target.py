class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)

        def dfs(u, curr_path_node):
            if u == n-1:
                ans.append(list(curr_path_node))
                return
            
            for v in graph[u]:
                curr_path_node.append(v)
                dfs(v, curr_path_node)
                curr_path_node.pop()

        dfs(0, [0])
        return ans

            
