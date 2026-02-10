"""
[[0,5,0,0]
 [1,4,1,0]
 [0,0,3,2]
 [1,2,1,0]]

 [[0,-1,0,0]
 [-1,-1,-1,0]
 [0,0,-2,-2]
 [-3,-3,-3,0]]


[[0,1,0,0]
 [1,1,1,0]
 [0,0,0,0]
 [0,0,0,0]]

 maxVal = 11

 Q's to ask:
 1. Will there be any negative numbers?




"""

def no_of_island(arr):
    rows = len(arr)
    cols = len(arr[0])
    visited = set()
    negative_mark = -1

    # best pair: (maxVal, island_id_that_gave_maxVal)
    best = (0, None)
    def dfs(row, col):
        if row<0 or row>=rows or col<0 or col>=cols or arr[row][col] == 0 or (row, col) in visited:
            return 0
        visited.add((row, col))
        total = arr[row][col]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # N,E,W,S
        for dx, dy in directions:
            edx, edy = row + dx, col + dy
            total += dfs(edx, edy)
        # island_id
        arr[row][col] = negative_mark
        return total


    for r in range(rows):
        for c in range(cols):
            if arr[r][c]>0 and (r,c) not in visited:
                current_id = negative_mark
                island_sum = dfs(r, c)
                if island_sum > best[0]:
                    best = (island_sum, current_id)
                negative_mark -= 1

    # Convert grid
    max_val, max_id = best
    for r in range(rows):
        for c in range(cols):
            arr[r][c] = 1 if arr[r][c]==max_id else 0

    return max_val, arr


nums = [[0,5,0,0],
        [1,4,1,0],
        [0,0,0,0],
        [1,2,1,0]]

max_sum, labeled = no_of_island(nums)
print(max_sum)
print(labeled)