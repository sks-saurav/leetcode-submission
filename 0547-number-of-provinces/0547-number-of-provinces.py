class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Solution 1 (DFS)
        n = len(isConnected)
        visited = [False] * n

        def dfs(u):
            if visited[u]:
                return

            visited[u] = True
            for v in range(n):
                if isConnected[u][v]:
                    dfs(v)

        
        proviences = 0
        for city in range(n):
            if not visited[city]:
                proviences += 1
                dfs(city)

        return proviences