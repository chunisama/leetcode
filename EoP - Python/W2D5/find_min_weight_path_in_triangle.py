# Define a path in the triangle to be a sequence of entries in the triangle in which adjacent entries in the sequence 
# correspond to entries that are adjacent in the triangle. The path must start at the top, descend the triangle 
# continuously, and end with an entry on the bottom row. The weight of a path is the sum of the entries.
# Write a program that takes as input a triangle of numbers and retums the weight of a minimum weight path.

arr = [
        [2],
       [4,1],
      [8,5,6],
     [4,2,6,2],
    [1,5,2,3,4]
]

# O(n^2)
def find_min_weight_path_in_triangle(triangle):
  table = [[] for i in range(len(triangle))]
  table[0].append(triangle[0][0])
  for i in range(1, len(triangle)):
    row = triangle[i]
    for j in range(len(row)):
      if j == 0:
        table[i].append(table[i - 1][j] + triangle[i][j])
      elif j == len(row) - 1:
        table[i].append(table[i - 1][-1] + triangle[i][j])
      else:
        path_1 = table[i - 1][j - 1] + triangle[i][j]
        path_2 = table[i - 1][j] + triangle[i][j]
        table[i].append(min(path_1, path_2))
  return min(table[-1])

print(find_min_weight_path_in_triangle(arr))

