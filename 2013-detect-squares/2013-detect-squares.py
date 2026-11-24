class DetectSquares:
    def __init__(self):
        self.point_counts = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.point_counts[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        x1, y1 = point
        total = 0

        for (x2, y2), c2 in self.point_counts.items():
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