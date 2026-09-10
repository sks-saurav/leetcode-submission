from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        # For each index, store a list of [snap_id, value]
        # Initialized with snapshot 0 having value 0
        self.history = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        # If the last recorded change was during the current snapshot, overwrite it
        if self.history[index][-1][0] == self.snap_id:
            self.history[index][-1][1] = val
        else:
            self.history[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        records = self.history[index]
        
        # Binary search for the largest recorded snap_id <= target snap_id
        # We search for [snap_id + 1] to find the insertion point of anything strictly greater
        idx = bisect_right(records, [snap_id, float('inf')]) - 1
        return records[idx][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)