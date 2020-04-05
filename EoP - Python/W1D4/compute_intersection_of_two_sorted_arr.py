# Write a program which takes as input two sorted arrays, and returns a new array 
# containing elements that are present in both of the input arrays. 
# The input arrays may have duplicate entries, but the returned array should be free of 
# duplicates. 
# For example, the input is (2,3,3,5,5,6,7,7,8,12) and (5,5,6,8 ,8,9,70,10), 
# your output should be (5, 6, 8).

# naive approach
def find_intersect(arr_1, arr_2):
  checkSet = set(arr_1)
  result = []
  for data in checkSet:
    if data in arr_2:
      result.append(data)
  return result

# optimal approach
import bisect
def find_intersect(arr_1, arr_2):
  check_set = set(arr_1)
  result = []
  for key in check_set:
    idx = bisect.bisect_left(arr_2, key)
    if (idx < len(arr_2)) and (arr_2[idx] == key):
      result.append(key)
  return result

