from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for a, b, cost in flights:
            adj[a].append((b, cost))

        heap = [(0, 0, src)]
        
        min_stops = [float('inf')] * n

        while heap:
            cost, stop, curr = heapq.heappop(heap)
            if curr == dst:
                return cost
            if stop >= min_stops[curr]:
                continue
            min_stops[curr] = stop

            if stop <= k:
                for nxt, price in adj[curr]:
                    heapq.heappush(heap, (cost + price, stop + 1, nxt))

        return -1