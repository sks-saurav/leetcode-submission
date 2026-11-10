class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]

        def dfs(x, y, stx, sty, shape):
            if visited[x][y] or grid[x][y] == 0:
                return

            visited[x][y] = True
            shape.add((x-stx, y-sty))
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < row and 0 <= ny < col:
                    dfs(nx, ny, stx, sty, shape)

        unique_shape = set()
        for x in range(row):
            for y in range(col):
                curr_shape = set()
                if not visited[x][y] and grid[x][y] == 1:
                    dfs(x, y, x, y, curr_shape)
                    unique_shape.add(frozenset(curr_shape))

        return len(unique_shape)
