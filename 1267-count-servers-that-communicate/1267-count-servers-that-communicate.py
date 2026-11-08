class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])

        rowServer = [0] * row
        colServer = [0] * col

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    rowServer[i] += 1
                    colServer[j] += 1

        ans = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (rowServer[i] > 1 or colServer[j] > 1):
                    ans += 1

        return ans
