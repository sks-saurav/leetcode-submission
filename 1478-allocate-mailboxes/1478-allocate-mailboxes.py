class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        n = len(houses)
        if k >= n:
            return 0
        
        houses.sort()
        
        # cost[i][j]: minimum distance to cover houses[i..j] with 1 mailbox
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + (houses[j] - houses[i])
        
        # dp[m][i]: min distance for first i houses using m mailboxes
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        
        # Base case: 1 mailbox for the first i houses
        for i in range(1, n + 1):
            dp[1][i] = cost[0][i - 1]
            
        # Transition: allocate m mailboxes
        for m in range(2, k + 1):
            for i in range(m, n + 1):
                for p in range(m - 1, i):
                    dp[m][i] = min(dp[m][i], dp[m - 1][p] + cost[p][i - 1])
                    
        return dp[k][n]