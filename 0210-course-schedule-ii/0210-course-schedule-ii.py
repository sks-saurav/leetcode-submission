class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BFS
        indeg = [0] * numCourses
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1

        que = deque()
        order = []
        for c in range(numCourses):
            if indeg[c] == 0:
                que.append(c)

        while que:
            curr = que.popleft()
            order.append(curr)

            for nxt in adj[curr]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    que.append(nxt)

        return order if len(order) == numCourses else []
        
        # DFS Approach / Cycle detection
        # adj = defaultdict(list)
        # for a, b in prerequisites:
        #     adj[b].append(a)

        # visited = [0] * numCourses

        # def dfs(u):
        #     visited[u] = 1

        #     for v in adj[u]:
        #         if visited[v] == 1:
        #             return False
        #         if visited[v] == 0:
        #             if not dfs(v):
        #                 return False

        #     visited[u] = 2
        #     return True

        # for u in range(numCourses):
        #     if visited[u] == 0:
        #         if not dfs(u):
        #             return False

        # return True