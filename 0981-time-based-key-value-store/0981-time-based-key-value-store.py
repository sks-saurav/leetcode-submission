from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.kv_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv_store:
            return ""

        arr = self.kv_store[key]

        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if arr[mid][0] <= timestamp:
                l = mid
            else:
                r = mid - 1

        return arr[l][1] if arr[l][0] <= timestamp else ""