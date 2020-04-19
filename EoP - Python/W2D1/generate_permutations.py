# Write a program which takes as input an array of distinct integers and generates all 
# permutations of that array. No permutation of the array may appear more than once.

# review 

# def generate_perms(arr, i = 0):
#   result = []
#   if i == len(arr) - 1:
#     result.append(arr.copy())
#     return
#   for j in range(i, len(arr)):
#     arr[i], arr[j] = arr[j], arr[i]
#     generate_perms(arr, i + 1)
#     arr[i], arr[j] = arr[j], arr[i]
#   return result

arr = [2,3,5,7]

# recursively
#          None  [2, 3, 5, 7]
#           2     [3. 5. 7]
#           3     [5, 7]
#           5      [7]
#           7      []


def generate_permutations(arr):
  result = []
  def dfs(permutated, decision_arr):
    if len(decision_arr) == 0: result.append(permutated[:]) # result = [[2,3,5,7]]
    for num in decision_arr:
      # decision = [3 ,5, 7] permutated = [2] => decision = [5, 7], permute = [2, 3] => decision = [7], permute [2,3,5]
      permutated.append(num) 
      # permutated = [2, 3] => [2, 3, 5] = [2, 3, 5, 7]
      # print(permutated)

      next_decision_arr = decision_arr[:] # next = [3, 5 ,7] = [5, 7] = [7]
      next_decision_arr.remove(num) # next = [5, 7] = [7] = []
      dfs(permutated, next_decision_arr) # => dfs([2], [3, 5, 7]) => dfs([2, 3], [5, 7]) => dfs([2,3,5], [7]) => dfs([2,3,5,7], [])
      permutated.pop() # permutated = [2, 3, 5]
  dfs([], arr)
  return result

print(generate_permutations(arr))