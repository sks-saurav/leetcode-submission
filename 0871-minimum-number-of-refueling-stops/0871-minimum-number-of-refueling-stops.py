class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []
        max_reach = startFuel
        stops = 0

        # Treat the target as a terminal station with 0 fuel
        for pos, fuel in stations + [[target, 0]]:
            # If we cannot reach the current station/target, refuel from the best past stations
            while max_reach < pos and max_heap:
                max_reach += -heapq.heappop(max_heap)
                stops += 1

            # If we still can't reach this position, reaching target is impossible
            if max_reach < pos:
                return -1

            heapq.heappush(max_heap, -fuel)

        return stops