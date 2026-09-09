# PREMIUM
# Approach 2
class HitCounter:
    def __init__(self):
        # We only need to track the last 300 seconds
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        # Map the timestamp to an index 0-299
        idx = timestamp % 300
        
        if self.times[idx] != timestamp:
            # If the timestamp at this index is old, overwrite it
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            # If it's the same timestamp, just increment the count
            self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        total_hits = 0
        for i in range(300):
            # Only count the hits if they happened within the last 300 seconds
            if timestamp - self.times[i] < 300:
                total_hits += self.hits[i]
        return total_hits

# Approach 1
# class HitCounter:

#     def __init__(self):
#         self.store = []

#     def hit(self, timestamp: int) -> None:
#         self.store.append(timestamp)

#     def getHits(self, timestamp: int) -> int:
#         timestamp -= 300
#         l, r = 0, len(self.store)
#         while l < r:
#             mid = (l+r) // 2
#             if self.store[mid] > timestamp:
#                 r = mid
#             else:
#                 l = mid+1

#         return len(self.store) - l


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)