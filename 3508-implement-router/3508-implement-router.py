class Router:
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.queue = deque()
        self.packet_set = set()
        # {'timestamps': list, 'start': int} tracking active packets per destination
        self.dest_packets = {}

    def _remove_oldest(self) -> tuple:
        """Helper function to remove and clean up the oldest packet in FIFO order."""
        packet = self.queue.popleft()
        self.packet_set.remove(packet)
        _, destination, _ = packet
        
        entry = self.dest_packets[destination]
        entry['start'] += 1
        
        # Periodic cleanup to prevent unbounded list growth
        if entry['start'] > 1024 and entry['start'] * 2 > len(entry['timestamps']):
            entry['timestamps'] = entry['timestamps'][entry['start']:]
            entry['start'] = 0
            
        return packet

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if self.memory_limit <= 0:
            return False

        packet = (source, destination, timestamp)
        
        if packet in self.packet_set:
            return False
        
        if len(self.queue) >= self.memory_limit:
            self._remove_oldest()
            
        self.packet_set.add(packet)
        self.queue.append(packet)
        
        if destination not in self.dest_packets:
            self.dest_packets[destination] = {'timestamps': [], 'start': 0}
        self.dest_packets[destination]['timestamps'].append(timestamp)
        
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        
        packet = self._remove_oldest()
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_packets:
            return 0
        
        entry = self.dest_packets[destination]
        timestamps = entry['timestamps']
        start_idx = entry['start']
        
        # Since timestamps arrive in non-decreasing order, the sublist is always sorted.
        left = bisect_left(timestamps, startTime, lo=start_idx)
        right = bisect_right(timestamps, endTime, lo=start_idx)
        
        return max(0, right - left)