"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        mp = defaultdict(int)
        for emp_sch in schedule:
            for s in emp_sch:
                mp[s.start] += 1
                mp[s.end] -= 1

        arr = [(k, mp[k]) for k in mp]
        arr.sort()
        p_busy_count = 0

        ans = []
        for idx, (ele, f) in enumerate(arr):
            curr_busy_count = p_busy_count + f
            if idx != 0 and idx != len(arr)-1:
                if curr_busy_count == 0:
                    ans.append(ele)
                elif curr_busy_count != 0 and p_busy_count == 0:
                    ans.append(ele)
            
            p_busy_count = curr_busy_count
        print(ans)

        final_res = []
        for i in range(0, len(ans), 2):
            final_res.append(Interval(ans[i], ans[i+1]))

        return final_res