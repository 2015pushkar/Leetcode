class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        orig = image[sr][sc]
        if orig == color:
            return image
        image[sr][sc] = color
        queue = collections.deque()
        visited = set()
        visited.add((sr,sc))
        queue.append((sr,sc))
        while queue:
            row, col = queue.popleft()
            directions = [[1,0],[0,-1],[-1,0],[0,1]]
            for dr,dc in directions:
                row_dr,col_dr = row+dr,col+dc
                if (row_dr in range(rows) and col_dr in range(cols) and image[row_dr][col_dr] == orig and (row_dr, col_dr) not in visited):
                    image[row_dr][col_dr] = color
                    queue.append((row_dr,col_dr))
                    visited.add((row_dr,col_dr))
        return image
        
        




            
                
        