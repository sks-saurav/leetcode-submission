class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.psum = [[0] * self.col for _ in range(self.row)]
        self._populatePsum(matrix)

    def _populatePsum(self, mat):
        for i in range(self.row):
            for j in range(self.col):
                self.psum[i][j] = mat[i][j] + (
                    (self.psum[i-1][j] if i > 0 else 0)
                    + (self.psum[i][j-1] if j > 0 else 0)
                    - (self.psum[i-1][j-1] if i > 0 and j > 0 else 0)
                )


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.psum[row2][col2]
            - (self.psum[row1-1][col2] if row1 > 0 else 0)
            - (self.psum[row2][col1-1] if col1 > 0 else 0)
            + (self.psum[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0)
        )
                    
                
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)