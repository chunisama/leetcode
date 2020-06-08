# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

def subsets(nums):
  def backtrack(first, curr):
    if len(curr) == j:
      # print(curr)
      result.append(curr[:])
    for i in range(first, len(nums)):
      curr.append(nums[i])
      backtrack(i + 1, curr)
      curr.pop()

  result = []
  for j in range(len(nums) + 1):
      backtrack(0, []) 
  return result

print(subsets([1,2,3]))