class Solution:
    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
            if k == 0:
                return 1.0
            
            dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]
            dp[0][row][col] = 1
            direction = [(1, 2), (1,-2), (-1,2), (-1,-2),(2, 1), (2,-1), (-2,1), (-2,-1)]

            for step in range(1, k+1):
                for x in range(n):
                    for y in range(n):
                        for dx, dy in direction:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n:
                                dp[step][x][y] += (dp[step-1][nx][ny]/8)


            ans = 0
            for r in dp[k]:
                ans += sum(r)

            return ans

        