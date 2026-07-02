# # BINARY INDEX TREE / FENWICK TREE
# class NumArray:

#     def __init__(self, nums: List[int]):
        

#     def update(self, index: int, val: int) -> None:
        

#     def sumRange(self, left: int, right: int) -> int:


# SEGMENT TREE
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.stree = [0 for _ in range(4 * self.n)]
        self.buildTree(nums, 0, 0, self.n-1)

    def update(self, index: int, val: int) -> None:
        return self._update(index, val, 0, 0, self.n-1)   

    def sumRange(self, left: int, right: int) -> int:
        return self._rangeSum(left, right, 0, 0, self.n-1)

    def buildTree(self, nums, index, st, end):
        if st == end: 
            self.stree[index] = nums[st]
            return self.stree[index]

        mid = st + (end - st) // 2
        left = self.buildTree(nums, 2*index + 1, st, mid)
        right = self.buildTree(nums, 2*index + 2, mid+1, end)
        self.stree[index] = left + right

        return self.stree[index]

    def _rangeSum(self, ql, qr, index, st, end):
        if qr < st or end < ql:
            return 0
            
        if ql <= st and qr >= end:
            return self.stree[index]

        mid = st + (end-st)//2
        left = self._rangeSum(ql, qr, 2*index+1, st, mid)
        right = self._rangeSum(ql, qr, 2*index+2, mid+1, end)

        return left+right

    def _update(self, qidx, qval, index, st, end):
        if qidx < st or qidx > end:
            return self.stree[index]

        if st == qidx and end == qidx:
            self.stree[index] = qval
            return self.stree[index]

        mid = st + (end-st)//2
        left = self._update(qidx, qval, 2*index+1, st, mid)
        right = self._update(qidx, qval, 2*index+2, mid+1, end)
        self.stree[index] = left + right
        return self.stree[index]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)