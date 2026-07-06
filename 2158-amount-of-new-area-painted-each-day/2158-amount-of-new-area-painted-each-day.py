# PREMIUM

class SegmentTree:
    def __init__(self, size: int):
        self.tree = [0] * (4 * size)
        self.lazy = [False] * (4 * size)

    def _push_down(self, node: int, left: int, right: int):
        if self.lazy[node]:
            mid = (left + right) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self.lazy[left_child] = True
            self.tree[left_child] = mid - left + 1
            
            self.lazy[right_child] = True
            self.tree[right_child] = right - mid
            self.lazy[node] = False

    def query(self, node: int, left: int, right: int, q_left: int, q_right: int) -> int:
        if q_right < left or q_left > right:
            return 0
        if q_left <= left and right <= q_right:
            return self.tree[node]
        
        self._push_down(node, left, right)
        mid = (left + right) // 2
        
        left_sum = self.query(2 * node + 1, left, mid, q_left, q_right)
        right_sum = self.query(2 * node + 2, mid + 1, right, q_left, q_right)
        return left_sum + right_sum

    def update(self, node: int, left: int, right: int, q_left: int, q_right: int):
        if q_right < left or q_left > right:
            return
        
        if q_left <= left and right <= q_right:
            self.tree[node] = right - left + 1
            self.lazy[node] = True
            return
        
        self._push_down(node, left, right)
        mid = (left + right) // 2
        self.update(2 * node + 1, left, mid, q_left, q_right)
        self.update(2 * node + 2, mid + 1, right, q_left, q_right)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]


class Solution:
    def amountPainted(self, paint: list[list[int]]) -> list[int]:
        MAX_POS = 50000
        tree = SegmentTree(MAX_POS)
        worklog = []
        
        for start, end in paint:
            q_left = start
            q_right = end - 1
            already_painted = tree.query(0, 0, MAX_POS, q_left, q_right)
            
            total_length = end - start
            new_area = total_length - already_painted
            worklog.append(new_area)
            
            if new_area > 0:
                tree.update(0, 0, MAX_POS, q_left, q_right)
                
        return worklog
