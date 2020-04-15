# Write a program that counts how many ways you can go from the top-left to the bottom-right 
# in a 2D array.


def number_of_ways(row, col):
  dp_table = [[1 for y in range(col)] for x in range(row)]
  for x in range(1, row):
    for y in range(1, col):
      dp_table[x][y] = dp_table[x][y - 1] + dp_table[x - 1][y]
  return dp_table[-1][-1]

print(number_of_ways(5,5))
  