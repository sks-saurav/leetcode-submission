class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        dist = [[float('inf')] * col for _ in range(row)]
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        que = deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    mat[i][j] = -1
                    que.append((i, j, 0))

        print(que)

        while que:
            x, y, step = que.popleft()
            dist[x][y] = min(dist[x][y], step)

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and mat[nx][ny] != -1:
                    mat[nx][ny] = -1
                    que.append((nx, ny, step+1))

        return dist

