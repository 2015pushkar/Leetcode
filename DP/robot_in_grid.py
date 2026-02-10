"""
Robot in a Grid:
1. Robot movement: right and down
2. direction: top left to the bottom right
 - Build from bottom-right backwards
- To know if you can reach a cell (r, c), the only ways into it are:
        - from (r-1, c) (down move came from above)
        - from (r, c-1) (right move came from left)
- Does a path exist to (r, c)?
    - path_to(r,c) = path_to(r-1,c) OR path_to(r,c-1)
- If you start from the destination you can recursively ask: can I reach you from one of your parents? and keep going until you hit (0,0)
- You could also start at (0,0) and go forward, but then you're in "explore all possible moves" - DFS/BFS.
- The books approach is more DP style, each cell depends on its parent
- Try to reach (0,0) by moving left-up
"""
def get_path_raw(maze):
    """
    MAZE: 2D list of booleans
    True => open cell
    False => blocked cell
    """
    if not maze or not maze[0]:
        return None
    path = []
    failed_points = set()
    if _get_path_raw(maze, len(maze)-1, len(maze[0])-1, path, failed_points):
        return path
    return None
def _get_path_raw(maze, row, col, path, failed_points):
    if row<0 or col<0 or not maze[row][col]:
        return False

    if (row,col) in failed_points:
        return False

    is_origin = (row == 0 and col == 0)

    # append a cell when we are sure it lies on a valid path
    if is_origin or _get_path_raw(maze, row-1, col, path, failed_points) or _get_path_raw(maze, row, col-1, path, failed_points):
        path.append((row, col))
        return True
    failed_points.add((row, col))
    return False

maze = [
    [True,  True,  True],
    [True,  False, False],
    [True,  True,  True]
]

print(get_path_raw(maze))



