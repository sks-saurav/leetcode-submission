# PREMIUM

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        row, col = len(maze), len(maze[0])
        directions = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]

        @cache
        def get_dest(u, v):
            res = []
            for dx, dy, inst in directions:
                dist = 0
                x, y = u, v
                while 0 <= x+dx < row and 0 <= y+dy < col and maze[x+dx][y+dy] == 0:
                    dist += 1
                    x += dx
                    y += dy
                    if x == hole[0] and y == hole[1]:
                        break
                if dist != 0:
                    res.append((x, y, dist, inst))
            return res

        best_paths = [[(float('inf'), "")] * col for _ in range(row)]
        heap = [(0, "", ball[0], ball[1])]
        best_paths[ball[0]][ball[1]] = (0, "")

        while heap:
            curr_dist, path_str, x, y = heappop(heap)
            if x == hole[0] and y == hole[1]:
                return path_str
           
            for nx, ny, n_dist, inst in get_dest(x, y):
                t_dist = curr_dist + n_dist
                t_path_str = path_str + inst
                if (t_dist, t_path_str) >= best_paths[nx][ny]:
                    continue

                best_paths[nx][ny] = (t_dist, t_path_str)
                heappush(heap, (t_dist, t_path_str, nx, ny))

        return "impossible"