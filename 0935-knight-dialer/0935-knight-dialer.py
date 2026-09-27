class Solution:
    def knightDialer(self, n: int) -> int:
        row,col = 4, 3
        MOD = int(1e9) + 7
        dp = [[[0] * col for _ in range(row)] for _ in range(n)]
        direction = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
        
        def isNotNum(x, y):
            return x == (row-1) and (y == 0 or y == (col-1))

        for i in range(row):
            for j in range(col):
                if isNotNum(i, j): continue
                dp[0][i][j] = 1

        for step in range(1, n):
            for x in range(row):
                for y in range(col):
                    if isNotNum(x, y): continue
                    
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < row and 0 <= ny < col and not isNotNum(nx, ny):
                            dp[step][x][y] = (dp[step][x][y] + dp[step-1][nx][ny]) % MOD

        ans = 0
        for r in dp[n-1]:
            ans = (ans + sum(r)) % MOD

        return ans
