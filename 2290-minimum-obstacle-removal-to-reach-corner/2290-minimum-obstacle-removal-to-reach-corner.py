class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        que = [(grid[0][0], 0, 0)]
        dist = [[float('inf')] * col for _ in range(row)]
        dist[0][0] = grid[0][0]


        while que:
            curr_dist, x, y = heappop(que)

            if x == row-1 and y == col-1:
                return curr_dist

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col:
                    new_dist = curr_dist + grid[nx][ny]
                    if new_dist < dist[nx][ny]:
                        heappush(que, (new_dist, nx, ny))
                        dist[nx][ny] = new_dist

        return -1


