# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]

from functools import cmp_to_key
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # OPTION 1:
        # def custom_cmp(a, b):
        #     if a[0] != b[0]:
        #         return a[0] - b[0]
        #     return a[1] - b[1]

        # intervals.sort(key = cmp_to_key(custom_cmp))

        # OPTION 2
        intervals.sort(key = cmp_to_key(
            lambda a, b: a[0]-b[0] if a[0] != b[0] else a[1]-b[1]
        ))
        
        ans = []
        ans.append(intervals[0])

        for st, end in intervals:
            ls, le = ans[-1]
            if st <= le:
                ans[-1][1] = max(end, le)
            else:
                ans.append([st,end])

        return ans
