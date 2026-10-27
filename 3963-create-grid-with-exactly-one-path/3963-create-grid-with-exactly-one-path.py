class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        grid = []
        for r in range(m):
            if r == 0:
                path = '.'*n
            else:
                path = ('#' * (n-1))  + '.'
            grid.append(path)

        return grid