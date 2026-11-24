class DetectSquares:
    def __init__(self):
        self.point_counts = {}
        self.adj = defaultdict(set)

    def add(self, point: list[int]) -> None:
        point = tuple(point)
        self.point_counts[point] = self.point_counts.get(point, 0) + 1
        self.adj[point[1]].add(point)

    def count(self, point: list[int]) -> int:
        x1, y1 = point
        total = 0

        for point2 in self.adj[y1]:
            x2, y2 = point2
            c2 = self.point_counts.get(point2, 0)
            if y1 == y2 and x1 != x2:
                d = abs(x2 - x1)
                total += (
                    c2
                    * self.point_counts.get((x1, y1 + d), 0)
                    * self.point_counts.get((x2, y1 + d), 0)
                )
                total += (
                    c2
                    * self.point_counts.get((x1, y1 - d), 0)
                    * self.point_counts.get((x2, y1 - d), 0)
                )

        return total