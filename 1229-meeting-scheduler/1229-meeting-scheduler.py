# PREMIUM

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        arr = []
        for st, end in slots1:
            arr.append((st, 1))
            arr.append((end, -1))

        for st, end in slots2:
            arr.append((st, 1))
            arr.append((end, -1))

        arr.sort()
        availability = 0
        last_time = 0

        for t, d in arr:
            if availability == 2 and (t-last_time) >= duration:
                return [last_time, last_time+duration]

            last_time = t
            availability += d

        return []



        