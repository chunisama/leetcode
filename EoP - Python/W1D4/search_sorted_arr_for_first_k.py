# Write a method that takes a sorted array and a key and returns the index of the first 
# occurrence of that key in the array. return -1 if the key does not appear in the array. 
# For example, when applied to the array in example, your algorithm should return 3 if 
# the given key is 108; if it is 285, your algorithm should return 6.

# Ex: 
arr = [-14, -10, 2, 108, 108, 245, 285, 285, 285, 401]


# recursive
def find_target_idx(arr, target, lower = 0, higher = len(arr) - 1):
  if lower == higher: return -1
  middle_idx = (lower + higher) // 2
  if target < arr[middle_idx]:
    return find_target_idx(arr, target, lower, middle_idx)
  elif target > arr[middle_idx]:
    return find_target_idx(arr, target, middle_idx + 1, higher)
  else:
    i = 1
    while arr[middle_idx] == arr[middle_idx - i]:
      i += 1
    return middle_idx - i + 1

# iterative
def find_target_idx(arr, target):
  left = 0
  right = len(arr) - 1
  result = - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] > target:
      right = mid - 1
    elif arr[mid] == target:
      result = mid
      right = mid - 1 # nothing to the right of mid can be solution
    else: # arra[mid] < k
      left = mid + 1
  return result

# print()
print(find_target_idx(arr, 108))
