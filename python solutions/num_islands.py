# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        def dfs(grid, i, j):
            if 0 <= i < row and 0 <= j < col and grid[i][j] == "1":
                grid[i][j] = "2"
                dfs(grid, i - 1, j)
                dfs(grid, i + 1, j)
                dfs(grid, i, j - 1)
                dfs(grid, i, j + 1)
        row = len(grid)
        col = len(grid[0])
        count = 0
      
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
        return count