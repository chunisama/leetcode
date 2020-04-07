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

# import collections
# def find_smallest_sub_arr(arr, bounds):
#   left, right = 0, 0
#   remaining_ele_to_cover = len(bounds)
#   counter = collections.Counter(bounds)
#   for ele in arr:
#     if arr[left] in counter:
#       while remaining_ele_to_cover != 0:
#         right += 1
#       if arr[right] in counter:




