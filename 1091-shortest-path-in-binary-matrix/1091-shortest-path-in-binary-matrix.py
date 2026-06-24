class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:  return -1
        if n == 1:  return 1

        direction = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        que = deque([(0, 0, 1)])

        while que:
            x, y, step = que.popleft()

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    if nx == n-1 and ny == n-1:
                        return step + 1

                    grid[nx][ny] = 1
                    que.append((nx, ny, step+1))

        return -1



