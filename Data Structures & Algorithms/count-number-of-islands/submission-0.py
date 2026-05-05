class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Basic DFS Search

        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def traverse(i: int, j: int) -> None:
            grid[i][j] = "0"

            if i+1 < ROWS and grid[i+1][j] == "1":
                traverse(i+1,j)
            if i-1 >= 0 and grid[i-1][j] == "1":
                traverse(i-1,j)
            if j+1 < COLS and grid[i][j+1] == "1":
                traverse(i,j+1)
            if j-1 >=0 and grid[i][j-1] == "1":
                traverse(i,j-1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    traverse(i,j)
                    islands+=1
                    print(grid)
        
        return islands