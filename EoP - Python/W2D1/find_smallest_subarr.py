# Write a program which takes an array of strings and a set of strings, 
# and return the indices of the starting and ending index of a shortest subarray of the 
# given array that "covers" the set, i.e., contains all strings in the set.

# ex) 
# arr = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
# set = {'banana', 'cat'}
# output: ['banana', 'apple', 'cat'] => shortest sub_arr covering that set

# counter = {
#   banana : 1,
#   cat : 1
# }

# review

# use sliding window => two pointers: left, right => 0, 0
# increment left pointer until i visit banana
# increment right pointer until i visit cat

from collections import Counter
def find_smallest_sub_arr(arr, keys):
  length_of_sub = float('inf')
  for idx, word in enumerate(arr):
    curr_length = 1
    if word in keys:
      words_to_cover = Counter(keys)
      while words_to_cover and idx < len(arr): 
        if arr[idx] in words_to_cover:
          words_to_cover.remove(arr[idx])
        curr_length += 1
        idx += 1
      length_of_sub = min(curr_length, length_of_sub)
  return length_of_sub


