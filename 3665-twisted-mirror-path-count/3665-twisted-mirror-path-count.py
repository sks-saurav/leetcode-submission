class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = int(1e9) + 7

        def trace(r: int, c: int, d: str):
            while True:
                if d == 'R':
                    nr, nc = r, c + 1
                else:
                    nr, nc = r + 1, c

                if not (0 <= nr < m and 0 <= nc < n):
                    return None  # Out of bounds: invalid path

                if nr == m - 1 and nc == n - 1:
                    return (nr, nc)

                if grid[nr][nc] == 1:
                    if d == 'R':
                        r, c, d = nr, nc, 'D'
                    else:
                        r, c, d = nr, nc, 'R'
                else:
                    return (nr, nc)

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0:
                    continue
                # Destination reached; no further moves
                if r == m - 1 and c == n - 1:
                    continue

                for move in ('R', 'D'):
                    dest = trace(r, c, move)
                    if dest is not None:
                        nr, nc = dest
                        dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD

        return dp[m - 1][n - 1]