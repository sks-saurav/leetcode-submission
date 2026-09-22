class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        
        # Initialize a DP table with infinity
        # We add an extra row and column to easily handle edge boundaries
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        
        # Base cases: just outside the bottom-right cell, you need 1 health to survive
        dp[rows][cols-1] = 1
        dp[rows-1][cols] = 1
        
        # Traverse backward from bottom-right to top-left
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                # The minimum health needed if we go right or down
                min_health_needed = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                
                # Health can never drop below 1. If a room has a huge health potion,
                # min_health_needed might become 0 or negative, but we still need at least 1 HP to be alive.
                dp[i][j] = max(1, min_health_needed)
                
        return dp[0][0]