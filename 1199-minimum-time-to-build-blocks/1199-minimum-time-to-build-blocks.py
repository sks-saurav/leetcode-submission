class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapq.heapify(blocks)
        
        # Keep merging the two smallest blocks until 1 is left
        while len(blocks) > 1:
            # Pop the two smallest times
            x = heapq.heappop(blocks)
            y = heapq.heappop(blocks)
            
            heapq.heappush(blocks, y + split)
            
        return blocks[0]