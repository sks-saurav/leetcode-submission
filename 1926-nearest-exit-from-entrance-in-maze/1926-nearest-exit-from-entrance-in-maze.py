from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        que = deque([entrance])
        step = 0
        n, m = len(maze), len(maze[0])
        visited = [[False] * m for _ in range(n)]
        visited[entrance[0]][entrance[1]] = True

        while que:
            ll = len(que)
            for _ in range(ll):
                x, y = que.popleft()
                if x == 0 or y == 0 or x == n-1 or y == m-1:
                    if not (x == entrance[0] and y == entrance[1]):
                        return step 

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if maze[nx][ny] == '.' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            que.append([nx, ny])

            step += 1

        return -1
