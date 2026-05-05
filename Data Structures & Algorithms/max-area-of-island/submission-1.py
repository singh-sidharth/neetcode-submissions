class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        ROWS, COLS = len(grid), len(grid[0])
        # Basic DFS Search
        def traverse(i: int, j: int) -> None:
            if (i < 0 or i == ROWS or j < 0 or
                j == COLS or grid[i][j] == 0
            ):
                
                return 0
            grid[i][j] = 0
            return (1 + traverse(i+1,j)+ 
             traverse(i-1,j)+
             traverse(i,j+1)+ 
             traverse(i,j-1))
           
        max_area = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    max_area = max(max_area, traverse(i,j))
        
        return max_area