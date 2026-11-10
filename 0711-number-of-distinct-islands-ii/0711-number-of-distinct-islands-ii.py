class Solution:
    def numDistinctIslands2(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        unique_islands = set()

        def dfs(x, y, current_island):
            if x < 0 or x >= row or y < 0 or y >= col or visited[x][y] or grid[x][y] == 0:
                return
            
            visited[x][y] = True
            current_island.append((x, y))
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(x + dx, y + dy, current_island)

        def get_canonical_shape(island):
            # Generate the 8 possible transformations
            shapes = [[] for _ in range(8)]
            for x, y in island:
                shapes[0].append((x, y))
                shapes[1].append((x, -y))
                shapes[2].append((-x, y))
                shapes[3].append((-x, -y))
                shapes[4].append((y, x))
                shapes[5].append((y, -x))
                shapes[6].append((-y, x))
                shapes[7].append((-y, -x))

            canonical = None
            for shape in shapes:
                shape.sort() # Sort to find the anchor point
                anchor_x, anchor_y = shape[0]
                
                # Normalize by shifting the anchor to (0, 0)
                normalized_shape = tuple((x - anchor_x, y - anchor_y) for x, y in shape)
                
                # Keep the lexicographically smallest shape
                if canonical is None or normalized_shape < canonical:
                    canonical = normalized_shape
                    
            return canonical

        for x in range(row):
            for y in range(col):
                if not visited[x][y] and grid[x][y] == 1:
                    current_island = []
                    dfs(x, y, current_island)
                    canonical = get_canonical_shape(current_island)
                    print(canonical)
                    unique_islands.add(canonical)

        return len(unique_islands)