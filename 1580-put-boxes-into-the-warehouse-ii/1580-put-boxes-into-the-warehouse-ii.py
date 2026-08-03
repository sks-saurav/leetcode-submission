class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        n = len(warehouse)
        ans = 0
        i, wa, wb = 0, 0, len(warehouse)-1
        boxes.sort(reverse=True)

        while i < len(boxes) and wa <= wb:
            if boxes[i] <= warehouse[wa]:
                wa += 1
                ans += 1
            elif boxes[i] <=  warehouse[wb]:
                wb -= 1
                ans += 1
            
            i += 1

        return ans