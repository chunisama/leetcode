# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below:

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num = 0
        n = len(grid[0])
        m = len(grid)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # checking first row or bottom neighbor
                    if r == 0 or grid[r-1][c] == 0:
                        print("+1")
                        num += 1
                    # checking last row or upper neighbor
                    if r == m-1 or grid[r+1][c] == 0:
                        print("+1")
                        num += 1
                    # checking first col or left neibhor
                    if c == 0 or grid[r][c-1] == 0:
                        print("+1")
                        num += 1
                    # checking last column or right neighbor
                    if c == n-1 or grid[r][c+1] == 0:
                        print("+1")
                        num += 1
        return num