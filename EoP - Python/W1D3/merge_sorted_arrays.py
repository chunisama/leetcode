# Write a program that takes as input a set of sorted sequences and computes the union 
# of these sequences as a sorted sequence. For example, if the input is <3,5,7>, (0,5), 
# and <0,6,28>, then the output is (0, 0, 3, 5, 6, 6,7, 28).

#     0
#    /  \
#   3    5
#         \
#          7

# [0, 3, 5, 7]

# todo : redo

from heapq import heappush
def merge_sorted_arrays(sorted_arrays):
  # creating a min heap using heap class methods imported from python
  min_heap = []
  for sub_arr in sorted_arrays:
    for num in sub_arr:
      heappush(min_heap, num)
  
      
