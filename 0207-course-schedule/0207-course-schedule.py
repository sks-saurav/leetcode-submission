class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS Approach / Cycle detection
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)

        visited = [0] * numCourses

        def dfs(u):
            visited[u] = 1

            for v in adj[u]:
                if visited[v] == 1:
                    return False
                if visited[v] == 0:
                    if not dfs(v):
                        return False

            visited[u] = 2
            return True

        for u in range(numCourses):
            if visited[u] == 0:
                if not dfs(u):
                    return False

        return True