# The problem of finding the longest nondecreasing subsequence in a sequence of integers has implications to many 
# disciplines, including string matching and analyzing card games. As a concrete instance, the length of a longest 
# nondecreasing subsequence for the array in Figure 16.15 is 4. There are multiple longest nondecreasing subsequences, 
# e.g (0,4,70,14) and (0,2,6,9). Note that elements of non-decreasing subsequence are not required to immediately 
# follow each other in the original sequence.

# Write a Program that takes as input an array of numbers and returns the length of a longest nondecreasing subsequence 
# in the array.

# redo

#                                  i  j
arr =  [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
# table = [1, 2, 2, 3, 2, 3, 3, 4, 2, 4]
# return max of table

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

# arr = [-1, 3, 4, 5, 2,2,2,2]

def find_longest_non_decreasing_sub_sequence(arr):
  table = [1 for i in range(len(arr))]
  for j in range(1, len(arr)):
    for i in range(j):
      if arr[j] >= arr[i]:
        if table[j] == table[i]:
          table[j] += 1
        elif table[j] < table[i]:
          table[j] = table[i]
  return max(table)

print(find_longest_non_decreasing_sub_sequence(arr))