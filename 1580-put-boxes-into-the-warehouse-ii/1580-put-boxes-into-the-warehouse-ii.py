class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        n = len(warehouse)
        minHeight = float("inf")
        effectiveHeights = [0] * n

        for i in range(n):
            minHeight = min(minHeight, warehouse[i])
            effectiveHeights[i] = minHeight

        minHeight = float("inf")
        for i in range(n - 1, -1, -1):
            minHeight = min(minHeight, warehouse[i])
            effectiveHeights[i] = max(effectiveHeights[i], minHeight)

        ans = 0
        i, wa, wb = 0, 0, len(effectiveHeights)-1
        boxes.sort(reverse=True)

        while i < len(boxes) and wa <= wb:
            if boxes[i] <= effectiveHeights[wa]:
                wa += 1
                ans += 1
                i += 1
            elif boxes[i] <= effectiveHeights[wb]:
                wb -= 1
                ans += 1
                i += 1
            else:
                i += 1

        return ans