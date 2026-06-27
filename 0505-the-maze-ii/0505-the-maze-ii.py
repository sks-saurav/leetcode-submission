# PREMIUM

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        @cache
        def get_dest(u, v):
            res = []
            for dx, dy in direction:
                dist = 0
                x, y = u, v
                while 0 <= x+dx < row and 0 <= y+dy < col and maze[x+dx][y+dy] == 0:
                    dist += 1
                    x, y = x + dx, y + dy

                if dist != 0:
                    res.append((x, y, dist))

            return res

        
        dist = [[float('inf')]*col for _ in range(row)]
        heap = [(0, start[0], start[1])]
        dist[start[0]][start[1]] = 0


        while heap:
            curr_dist, x, y = heappop(heap)
            if x == destination[0] and y == destination[1]:
                return curr_dist

            for nx, ny, n_dist in get_dest(x, y):
                t_dist = curr_dist + n_dist
                if t_dist >= dist[nx][ny]:
                    continue

                dist[nx][ny] = t_dist
                heappush(heap, (t_dist, nx, ny))

        return -1



