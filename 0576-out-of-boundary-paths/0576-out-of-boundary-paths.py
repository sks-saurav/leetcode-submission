class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        
        # dp[k][i][j] = number of ways to reach cell (i, j) in exactly k moves
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1
        
        total_paths = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for k in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    if dp[k - 1][i][j] == 0:
                        continue
                    
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        
                        # If the move steps out of bounds, count it toward the answer
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            total_paths = (total_paths + dp[k - 1][i][j]) % MOD
                        else:
                            # Otherwise, transition to the neighbor cell in the next move
                            dp[k][ni][nj] = (dp[k][ni][nj] + dp[k - 1][i][j]) % MOD
                            
        return total_paths

# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         MOD = int(1e9) + 7

#         @cache
#         def helper(x, y, moveLeft):
#             if x < 0 or x >= m or y < 0 or y >= n:
#                 return 1

#             if moveLeft == 0:
#                 return 0

#             direction = [(1,0),(-1,0),(0,1),(0,-1)]
#             ans = 0
#             for dx, dy in direction:
#                 nx, ny = x + dx, y + dy
#                 ans = (ans + helper(nx, ny, moveLeft-1)) % MOD
#             return ans

#         return helper(startRow, startColumn, maxMove)