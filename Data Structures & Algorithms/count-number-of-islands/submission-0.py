class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        count = 0

        def explore(r,c):
            row_bound = 0 <= r < ROWS
            col_bound = 0 <= c < COLS

            if not row_bound or not col_bound:
                return False
            if grid[r][c] == '0' or (r,c)  in visited:
                return False
            
            visited.add((r,c))

            explore(r-1,c)
            explore(r+1,c)
            explore(r,c+1)
            explore(r,c-1)

            return True

        for r in range(ROWS):
            for c in range(COLS):
                if explore(r,c):
                    count += 1
        return count