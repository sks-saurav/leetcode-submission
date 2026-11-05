class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row, col = len(picture), len(picture[0])
        rCount = [0] * row
        cCount = [0] * col

        for i in range(row):
            count = 0
            for j in range(col):
                count += (1 if picture[i][j] == 'B' else 0)
            rCount[i] = count

        for j in range(col):
            count = 0
            for i in range(row):
                count += (1 if picture[i][j] == 'B' else 0)
            cCount[j] = count

        ans = 0
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B' and rCount[i] == 1 and cCount[j] == 1:
                    ans += 1

        return ans