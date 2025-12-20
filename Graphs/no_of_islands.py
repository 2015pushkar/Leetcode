from collections import deque
def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    island = 0
    rows, cols = len(grid), len(grid[0])
    visited = set() # (row, col)

    def bfs(row, col):

        queue = deque()
        visited.add((row, col))
        queue.append((row, col))
        while queue:
            curr_row, curr_col = queue.popleft()
            directions = [[1,0], [-1,0], [0,-1], [0,1]]
            for dr,dc in directions:
                row_dr, col_dr = curr_row + dr, curr_col + dc
                if (row_dr in range(rows) and col_dr in range(cols) and grid[row_dr][col_dr] == "1" and (row_dr, col_dr) not in visited):
                    visited.add((row_dr, col_dr))
                    queue.append((row_dr, col_dr))

     # Visit every single cell
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in visited:
                bfs(row, col)
                island += 1
    return island
    



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","1"]
]
res = numIslands(grid)
print(res)