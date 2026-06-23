class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        que = deque()
        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(u, v):
            if grid[u][v] != 1:
                return
            grid[u][v] = -1
            que.append((u, v, 0))
            for dx, dy in direction:
                x, y = u + dx, v + dy
                if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                    dfs(x, y)

        break_outer = False
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break_outer = True
                    break
            if break_outer:
                break

        while que:
            u, v, step = que.popleft()
            for dx, dy in direction:
                x, y = u + dx, v + dy
                if 0 <= x < row and 0 <= y < col and grid[x][y] != -1:
                    if grid[x][y] == 1:
                        return step
                    grid[x][y] = -1
                    que.append((x, y, step+1))

        return -1

