from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        if rows == 0:
            return -1
        
        cols = len(grid[0])
        count = 0
        rotten = deque()
        
        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # update fresh oranges count
                    count += 1
        
        minutes_passed = 0
        
        while rotten and count > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                        
                    # update the fresh oranges count
                    count -= 1
                    
                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2
                    
                    # add the current rotten to the queue
                    rotten.append((xx, yy))

        return minutes_passed if count == 0 else -1