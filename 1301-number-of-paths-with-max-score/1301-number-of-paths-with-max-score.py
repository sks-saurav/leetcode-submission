class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MIN = float('-inf')
        MOD = int(1e9) + 7
        direction = [(1,0), (0,1), (1,1)]
        
        dist = [[MIN]*n for _ in range(n)]
        ways = [[0]*n for _ in range(n)]
        dist[n-1][n-1] = 0
        ways[n-1][n-1] = 1

        for x in range(n-1, -1, -1):
            for y in range(n-1, -1, -1):
                if board[x][y] == 'X':
                    continue

                val = int(board[x][y]) if board[x][y].isnumeric() else 0
                mval = MIN

                for dx, dy in direction:
                    px, py = x + dx, y + dy
                    if 0 <= px < n and 0 <= py < n:
                        cost = val + dist[px][py]
                        dist[x][y] = max(dist[x][y], cost)
                        mval = max(mval, dist[px][py])

                for dx, dy in direction:
                    px, py = x + dx, y + dy
                    if 0 <= px < n and 0 <= py < n:
                        if dist[px][py] == mval:
                            ways[x][y] = (ways[x][y] + ways[px][py]) % MOD

        return [dist[0][0] if dist[0][0] != MIN else 0, ways[0][0]]


