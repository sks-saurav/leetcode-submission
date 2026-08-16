#PREMIUM

class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return
        
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.matrix = matrix
        self.tree = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
        for r in range(self.rows):
            for c in range(self.cols):
                self._update(r + 1, c + 1, matrix[r][c])

    def _update(self, row, col, delta):
        r = row
        while r <= self.rows:
            c = col
            while c <= self.cols:
                self.tree[r][c] += delta
                c += c & (-c)
            r += r & (-r)

    def _query(self, row: int, col: int) -> int:
        s = 0
        r = row
        while r > 0:
            c = col
            while c > 0:
                s += self.tree[r][c]
                c -= c & (-c)
            r -= r & (-r)
        return s

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self._update(row+1, col+1, delta)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Using 2D Inclusion-Exclusion Principle
        return (self._query(row2 + 1, col2 + 1) 
              - self._query(row1, col2 + 1) 
              - self._query(row2 + 1, col1) 
              + self._query(row1, col1))


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)