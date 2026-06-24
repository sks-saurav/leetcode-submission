class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0

        def dfs(x, y):
            grid[x][y] = 0
            connected, count = False, 1
            if x == 0 or x == row-1 or y == 0 or y == col-1:
                connected = True

            for dx, dy in [(1,0),(-1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                    t_conn, t_cnt = dfs(nx, ny)
                    connected = connected or t_conn
                    count += t_cnt

            return connected, count

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    connected, count = dfs(x, y)
                    if not connected:
                        ans += count

        return ans

