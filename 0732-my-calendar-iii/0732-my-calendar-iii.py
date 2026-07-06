from collections import defaultdict

class SegmentTree:
    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, qst, qend, qval, tst, tend, tidx):
        # qst           qend
        #     tst  tend
        if qst <= tst and tend <= qend:
            self.tree[tidx] += qval  # ADD qval, don't overwrite
            self.lazy[tidx] += qval  # ADD qval, don't overwrite
            return

        if tend < qst or qend < tst:
            return

        mid = (tst + tend) // 2
        self.push_down(tidx)
        
        self.update(qst, qend, qval, tst, mid, 2*tidx+1)
        self.update(qst, qend, qval, mid+1, tend, 2*tidx+2)
        self.tree[tidx] = max(self.tree[2*tidx+1], self.tree[2*tidx+2])

    def push_down(self, idx):
        if idx in self.lazy:
            l_child, r_child = 2*idx+1, 2*idx+2

            val = self.lazy[idx]
            del self.lazy[idx]

            # Propagate by ADDING to the children
            self.tree[l_child] += val
            self.tree[r_child] += val

            self.lazy[l_child] += val
            self.lazy[r_child] += val


class MyCalendarThree:
    def __init__(self):
        self.max_int = 10**9
        self.stree = SegmentTree()

    def book(self, startTime: int, endTime: int) -> int:
        self.stree.update(startTime, endTime - 1, 1, 0, self.max_int, 0)
        # The root node (index 0) always holds the maximum value for the whole tree
        return self.stree.tree[0]