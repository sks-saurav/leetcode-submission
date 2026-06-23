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

        def get_first_island_cell():
            for r in range(row):
                for c in range(col):
                    if grid[r][c] == 1:
                        return r, c
            return -1, -1

        start_r, start_c = get_first_island_cell()
        dfs(start_r, start_c)

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

