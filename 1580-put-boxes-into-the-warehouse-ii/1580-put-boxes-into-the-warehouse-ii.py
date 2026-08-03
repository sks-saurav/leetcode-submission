class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        l = list(warehouse)
        r = list(warehouse)

        for i in range(1, len(warehouse)):
            l[i] = min(l[i], l[i-1])

        for i in range(len(warehouse)-2, -1, -1):
            r[i] = min(r[i], r[i+1])

        for i in range(len(warehouse)):
            warehouse[i] = max(l[i], r[i])

        ans = 0
        i, j = 0, 0
        boxes.sort(reverse=True)
        warehouse.sort(reverse=True)

        while i < len(warehouse) and j < len(boxes):
            if boxes[j] <= warehouse[i]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1

        return ans