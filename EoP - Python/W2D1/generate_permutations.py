# Write a program which takes as input an array of distinct integers and generates all 
# permutations of that array. No permutation of the array may appear more than once.

# review 

def generate_perms(arr, i = 0):
  result = []
  if i == len(arr) - 1:
    result.append(arr.copy())
    return
  for j in range(i, len(arr)):
    arr[i], arr[j] = arr[j], arr[i]
    generate_perms(arr, i + 1)
    arr[i], arr[j] = arr[j], arr[i]
  return result
