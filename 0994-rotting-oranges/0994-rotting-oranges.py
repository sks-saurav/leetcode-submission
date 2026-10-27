class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count, n, m = 0, len(grid), len(grid[0])
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        time = 0
        if count == 0: return time
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        while q:
            l = len(q)
            while l > 0:
                x,y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= 0 and ny >= 0 and nx < n and ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        count -= 1
                l -= 1
            time += 1
        
        if count != 0:
            return -1
        return time-1