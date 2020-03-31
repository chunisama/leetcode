# Consider the following two rules to an array of characters and a variable size denotes
# the number of elements that the operations apply to
# 1. replace each "a" by two "d"s => [a] => [d, d]
# 2. delete each entry containing "b"

# input: size = 4, [a, c, d, b, b, c, a] => [d, d, c, d, c, d, d]
# iterate thru the array; have conditionals checking if char is "a" or if char is "b"
# counter to check how many operations have been done once my counter hits my size; break the loop
# if char is a => insert two ds at that index
# if char is b => delete b at that index
# O(n)

# O(n^2) naive approach
def replace_and_remove(size, arr):
  counter = 0
  for idx in range(len(arr) - 1):
    if counter is size: break
    if arr[idx] is "a":
      arr[idx] = "d"
      arr.insert(idx, "d")
    elif arr[idx] is "b":
      arr.pop(idx)
  return arr

# O(n) optimized approach

def replace_and_remove(size, arr):
  result = []
  counter = 0
  