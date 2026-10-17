class Solution:
    def maxKilledEnemies(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        row_hits = 0
        col_hits = [0] * n
        max_enemies = 0

        for i in range(m):
            for j in range(n):
                # Recalculate row enemies if at the start or after a wall
                if j == 0 or grid[i][j - 1] == 'W':
                    row_hits = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row_hits += 1
                        k += 1

                # Recalculate column enemies if at the top or after a wall
                if i == 0 or grid[i - 1][j] == 'W':
                    col_hits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_hits[j] += 1
                        k += 1

                if grid[i][j] == '0':
                    max_enemies = max(max_enemies, row_hits + col_hits[j])

        return max_enemies