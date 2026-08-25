# PREMIUM
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        if not peaks: 
            return 0

        c = collections.Counter()
        for x, y in peaks:
            c[(x, y)] += 1

        peaks = sorted(c.keys())    

        def within(pa, pb):                                 # return True if `pb` is within `pa`
            x1, y1 = pa
            x2, y2 = pb 
            b1 = y1 - x1
            b2 = y1 + x1
            return y2 <= x2 + b1 and y2 <= -x2 + b2

        n = len(peaks)
        stack = [tuple(peaks[0])]

        for x, y in peaks[1:]:
            while stack and within([x, y], stack[-1]):      # while previous point is `within` the current point 
                stack.pop()
            if not stack or not within(stack[-1], [x, y]):  # if current point is `within` the previous point
                stack.append((x, y))
                
        return len([p for p in stack if c[p] == 1])         # eliminate repeats and sort          