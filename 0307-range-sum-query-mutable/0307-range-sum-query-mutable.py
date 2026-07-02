# # BINARY INDEX TREE / FENWICK TREE
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums) + 1
        self.nums = [0] + nums # making it 1 index
        self.tree = [0 for _ in range(self.n)]
        
        self.build_tree()

    def rsb(self, i):
        return i & -i

    def build_tree(self): # O(n)
        for i in range(1, self.n):
            self.tree[i] = self.nums[i]
        
        for child in range(1, self.n):
            parent = child + self.rsb(child)
            if parent < self.n:
                self.tree[parent] += self.tree[child]

    def update(self, index: int, val: int) -> None:
        i = index+1 # nums is converted to 1 based index
        delta = val - self.nums[i] 
        self.nums[i] = val

        while i < self.n:
            self.tree[i] += delta
            i += self.rsb(i)

    def get_prefix_sum(self, index):
        i = index+1 # nums is converted to 1 based index
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= self.rsb(i)
        return ans

    def sumRange(self, left: int, right: int) -> int:
        return self.get_prefix_sum(right) - self.get_prefix_sum(left-1)

# # SEGMENT TREE
# class NumArray:
#     def __init__(self, nums: List[int]):
#         self.n = len(nums)
#         self.stree = [0 for _ in range(4 * self.n)]
#         self.buildTree(nums, 0, 0, self.n-1)

#     def update(self, index: int, val: int) -> None:
#         return self._update(index, val, 0, 0, self.n-1)   

#     def sumRange(self, left: int, right: int) -> int:
#         return self._rangeSum(left, right, 0, 0, self.n-1)

#     def buildTree(self, nums, index, st, end):
#         if st == end: 
#             self.stree[index] = nums[st]
#             return self.stree[index]

#         mid = st + (end - st) // 2
#         left = self.buildTree(nums, 2*index + 1, st, mid)
#         right = self.buildTree(nums, 2*index + 2, mid+1, end)
#         self.stree[index] = left + right

#         return self.stree[index]

#     def _rangeSum(self, ql, qr, index, st, end):
#         if qr < st or end < ql:
#             return 0
            
#         if ql <= st and qr >= end:
#             return self.stree[index]

#         mid = st + (end-st)//2
#         left = self._rangeSum(ql, qr, 2*index+1, st, mid)
#         right = self._rangeSum(ql, qr, 2*index+2, mid+1, end)

#         return left+right

#     def _update(self, qidx, qval, index, st, end):
#         if qidx < st or qidx > end:
#             return self.stree[index]

#         if st == qidx and end == qidx:
#             self.stree[index] = qval
#             return self.stree[index]

#         mid = st + (end-st)//2
#         left = self._update(qidx, qval, 2*index+1, st, mid)
#         right = self._update(qidx, qval, 2*index+2, mid+1, end)
#         self.stree[index] = left + right
#         return self.stree[index]

# # Your NumArray object will be instantiated and called as such:
# # obj = NumArray(nums)
# # obj.update(index,val)
# # param_2 = obj.sumRange(left,right)