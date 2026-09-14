class Block:
    def __init__(self, mId, st, end):
        self.mId = mId
        self.st = st
        self.end = end
        self.isFree = False

    def __lt__(self, other):
        if self.st != other.st:
            return self.st < other.st
        else:
            return self.end > other.end

class Allocator:
    def __init__(self, n: int):
        self.dict = defaultdict(list)
        self.heap = [Block(-1, n, float('inf'))]

    def allocate(self, size: int, mID: int) -> int:
        ans = -1
        temp = []
        prevSt = 0

        while self.heap:
            mb = heappop(self.heap)
            available = (prevSt, mb.st-1)

            if mb.isFree:
                available = (prevSt, mb.end)
            else:
                temp.append(mb)
                prevSt = mb.end+1

            if (available[1] - available[0] + 1) >= size:
                newBlock = Block(mID, available[0], available[0]+size-1)
                temp.append(newBlock)
                self.dict[mID].append(newBlock)
                ans = newBlock.st
                break

        for b in temp:
            heappush(self.heap, b)

        return ans

    def freeMemory(self, mID: int) -> int:
        freedUnit = 0
        if mID not in self.dict:
            return freedUnit

        for block in self.dict[mID]:
            block.isFree = True
            freedUnit += (block.end - block.st + 1)

        del self.dict[mID]
        return freedUnit

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)