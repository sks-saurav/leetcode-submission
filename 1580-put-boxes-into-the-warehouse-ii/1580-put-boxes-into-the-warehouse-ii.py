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
        i, wa, wb = 0, 0, len(warehouse)-1
        boxes.sort(reverse=True)

        while i < len(boxes) and wa <= wb:
            if boxes[i] <= warehouse[wa]:
                wa += 1
                ans += 1
                i += 1
            elif boxes[i] <= warehouse[wb]:
                wb -= 1
                ans += 1
                i += 1
            else:
                i += 1

        return ans