class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        islands: int = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(i, j, m, n, grid)

        return islands

    def dfs(self, i: int, j: int, m: int, n: int, mat: list[list[int]]) -> None:

        if i < 0 or j < 0 or i >= m or j >= n:
            return

        if mat[i][j] == "0" or mat[i][j] == "-1":
            return 

        mat[i][j] = "-1" # visited
        self.dfs(i, j+1, m, n, mat) # move right
        self.dfs(i+1, j, m, n, mat) # move down
        self.dfs(i, j-1, m, n, mat) # move left
        self.dfs(i-1, j, m, n, mat) # move up