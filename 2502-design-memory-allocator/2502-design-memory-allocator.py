# # Sol 1
# class Block:
#     def __init__(self, mId, st, end):
#         self.mId = mId
#         self.st = st
#         self.end = end
#         self.isFree = False

#     def __lt__(self, other):
#         if self.st != other.st:
#             return self.st < other.st
#         else:
#             return self.end > other.end

# class Allocator:
#     def __init__(self, n: int):
#         self.dict = defaultdict(list)
#         self.heap = [Block(-1, n, float('inf'))]

#     def allocate(self, size: int, mID: int) -> int:
#         ans = -1
#         temp = []
#         prevSt = 0

#         while self.heap:
#             mb = heappop(self.heap)
#             available = (prevSt, mb.st-1)

#             if mb.isFree:
#                 available = (prevSt, mb.end)
#             else:
#                 temp.append(mb)
#                 prevSt = mb.end+1

#             if (available[1] - available[0] + 1) >= size:
#                 newBlock = Block(mID, available[0], available[0]+size-1)
#                 temp.append(newBlock)
#                 self.dict[mID].append(newBlock)
#                 ans = newBlock.st
#                 break

#         for b in temp:
#             heappush(self.heap, b)

#         return ans

#     def freeMemory(self, mID: int) -> int:
#         freedUnit = 0
#         if mID not in self.dict:
#             return freedUnit

#         for block in self.dict[mID]:
#             block.isFree = True
#             freedUnit += (block.end - block.st + 1)

#         del self.dict[mID]
#         return freedUnit


# SOL 2
class Allocator:
    def __init__(self, n: int):
        # -1 represents a free memory unit
        self.memory = [-1] * n

    def allocate(self, size: int, mID: int) -> int:
        free_count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == -1:
                free_count += 1
                if free_count == size:
                    # We found a big enough block. Calculate the start index.
                    start_idx = i - size + 1
                    # Fill the memory block with mID
                    for j in range(start_idx, i + 1):
                        self.memory[j] = mID
                    return start_idx
            else:
                # Reset contiguous count if we hit an occupied block
                free_count = 0
                
        return -1

    def freeMemory(self, mID: int) -> int:
        freed_units = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = -1
                freed_units += 1
                
        return freed_units