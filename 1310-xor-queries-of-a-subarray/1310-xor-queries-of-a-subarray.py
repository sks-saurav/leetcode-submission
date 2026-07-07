class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4*self.n)
        self.build_tree(nums)

    def build_tree(self, nums):
        for i, val in enumerate(nums):
            self.update(i, val, 0, self.n-1, 0)

    def update(self, qidx, qval, tst, tend, tidx):
        if qidx < tst or qidx > tend:
            return
        if qidx == tst and qidx == tend:
            self.tree[tidx] = qval
            return

        mid = (tst + tend)//2
        self.update(qidx, qval, tst, mid, 2*tidx+1)
        self.update(qidx, qval, mid+1, tend, 2*tidx+2)
        self.tree[tidx] = self.tree[2*tidx+1] ^ self.tree[2*tidx+2]

    def query(self, qst, qend, tst, tend, tidx):
        # qst         qend
        #    tst  tend
        if qst <= tst and tend <= qend:
            return self.tree[tidx]
        if tend < qst or qend < tst:
            return 0

        mid = (tst + tend) // 2
        left = self.query(qst, qend, tst, mid, 2*tidx+1)
        right = self.query(qst, qend, mid+1, tend, 2*tidx+2)
        return left ^ right


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        stree = SegmentTree(arr)
        ans = []

        for st, end in queries:
            ans.append(stree.query(st, end, 0, len(arr)-1, 0))

        return ans