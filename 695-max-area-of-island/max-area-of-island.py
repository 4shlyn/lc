class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        m = 0
        visited = set()
        def dfs(r,c):
            s=1
            if 0 > r or r >= rows or 0 > c or c >= cols:
                return 0
            if grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            
            s+=dfs(r+1,c)
            s+=dfs(r,c+1)
            s+=dfs(r-1,c)
            s+=dfs(r,c-1)
        
            return s

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    m = max(dfs(r,c),m)
        return m
