class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Solution 1 (DFS)
        # n = len(isConnected)
        # visited = [False] * n

        # def dfs(u):
        #     if visited[u]:
        #         return

        #     visited[u] = True
        #     for v in range(n):
        #         if isConnected[u][v]:
        #             dfs(v)

        
        # proviences = 0
        # for city in range(n):
        #     if not visited[city]:
        #         proviences += 1
        #         dfs(city)

        # return proviences

        # Solution 2 (Union Find)
        n = len(isConnected)
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

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)


        distinct_p = set()
        for i in range(n):
            distinct_p.add(get_parent(i))

        return len(distinct_p)
