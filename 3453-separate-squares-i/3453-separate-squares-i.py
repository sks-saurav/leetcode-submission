class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l * l for _, _, l in squares)
        half_area = total_area / 2.0

        # Map y-coordinate -> change in active total width
        events = defaultdict(int)
        for _, y, l in squares:
            events[y] += l        # Enter square: width increases
            events[y + l] -= l    # Exit square: width decreases

        # Sort the distinct y-coordinates
        sorted_ys = sorted(events.keys())

        current_area = 0.0
        current_width = 0

        for i in range(len(sorted_ys) - 1):
            y_curr = sorted_ys[i]
            y_next = sorted_ys[i + 1]

            current_width += events[y_curr]
            dy = y_next - y_curr
            slice_area = current_width * dy

            if current_area + slice_area >= half_area:
                # Target lies within this interval [y_curr, y_next]
                remaining = half_area - current_area
                return y_curr + (remaining / current_width)

            current_area += slice_area

        return float(sorted_ys[-1])

# class Solution:
#     def separateSquares(self, squares: List[List[int]]) -> float:

#         def getArea(yMax):
#             area = 0.0
#             for x, y, l in squares:
#                 if y < yMax:
#                     h = min(y+l, yMax)-y
#                     area += (l*h)

#             return area

#         halfArea = getArea(float('inf')) / 2
#         lo = min(y for _, y, _ in squares)
#         hi = max(y + l for _, y, l in squares)
        
#         for _ in range(50):
#             mid = (lo+hi) / 2.0
#             area = getArea(mid)
#             if area >= halfArea:
#                 hi = mid
#             else:
#                 lo = mid

#         return lo
