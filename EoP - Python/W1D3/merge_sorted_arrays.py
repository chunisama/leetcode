# Write a program that takes as input a set of sorted sequences and computes the union 
# of these sequences as a sorted sequence. For example, if the input is [3,5,7], [0,5], 
# and [0,6,28], then the output is (0, 0, 3, 5, 6, 6,7, 28).

#     0
#    /  \
#   3    5
#         \
#          7

# [-1, 0, 3, 5, 7,]

# todo : redo

# O(n^2)
import heapq 
def merge_sorted_arrays(sorted_arrays):
  # creating a min heap using heap class methods imported from python
  min_heap = []
  result = []
  for sub_arr in sorted_arrays:
    for num in sub_arr:
        heapq.heappush(min_heap, num)
  while min_heap:
    result.append(heapq.heappop(min_heap))
  print(result)

merge_sorted_arrays([[3, 5 ,7], [0, 5], [0, 6, 28]])

# O(nlogn) => flatten the 2d array then iterate across use min heap and extract the min 
# and push into a new arr return new answer
      
