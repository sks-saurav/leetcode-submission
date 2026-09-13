class MaxStack:
    def __init__(self):
        self.is_active = defaultdict(bool)
        self.stack = []
        self.heap = []
        self.timestamp = 0

    def _get_timestamp(self):
        self.timestamp += 1
        return self.timestamp

    def _heap_cleanup(self):
        while self.heap and not self.is_active[self.heap[0]]:
            heappop(self.heap)
    
    def _stack_cleanup(self):
        while self.stack and not self.is_active[self.stack[-1]]:
            self.stack.pop()

    def push(self, x: int) -> None:
        ele = (-x, -self._get_timestamp())
        self.stack.append(ele)
        heappush(self.heap, ele)
        self.is_active[ele] = True

    def pop(self) -> int:
        self._stack_cleanup()
        if not self.stack:
            return -1

        ele = self.stack.pop()
        del self.is_active[ele]

        return -ele[0]

    def top(self) -> int:
        self._stack_cleanup()
        if not self.stack:
            return -1

        ele = self.stack[-1]
        return -ele[0]
        
    def peekMax(self) -> int:
        self._heap_cleanup()
        if not self.heap:
            return -1

        ele = self.heap[0]
        return -ele[0]

    def popMax(self) -> int:
        self._heap_cleanup()
        if not self.heap:
            return -1

        ele = heappop(self.heap)
        del self.is_active[ele]
        return -ele[0]


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()