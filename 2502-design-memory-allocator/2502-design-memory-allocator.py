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
        self.n = n
        # Will store tuples of: (start_index, end_index, mID)
        # Always kept in sorted order based on start_index
        self.blocks = [] 

    def allocate(self, size: int, mID: int) -> int:
        prev_end = 0
        
        # Check the gaps between allocated blocks
        for i, (start, end, _) in enumerate(self.blocks):
            # Is the gap between the last block and this block large enough?
            if start - prev_end >= size:
                self.blocks.insert(i, (prev_end, prev_end + size, mID))
                return prev_end
            prev_end = end
            
        # If no gap was found between blocks, check the tail end of the memory
        if self.n - prev_end >= size:
            self.blocks.append((prev_end, prev_end + size, mID))
            return prev_end
            
        return -1

    def freeMemory(self, mID: int) -> int:
        freed_units = 0
        retained_blocks = []
        
        # Filter out the blocks matching the mID
        for start, end, block_id in self.blocks:
            if block_id == mID:
                freed_units += (end - start)
            else:
                retained_blocks.append((start, end, block_id))
                
        self.blocks = retained_blocks
        return freed_units