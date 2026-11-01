class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        def getArea(yMax):
            area = 0.0
            for x, y, l in squares:
                if y < yMax:
                    h = min(y+l, yMax)-y
                    area += (l*h)

            return area

        halfArea = getArea(float('inf')) / 2
        lo = min(y for _, y, _ in squares)
        hi = max(y + l for _, y, l in squares)
        
        for _ in range(50):
            mid = (lo+hi) / 2.0
            area = getArea(mid)
            if area >= halfArea:
                hi = mid
            else:
                lo = mid

        return lo
