# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:

# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example:

# Input: root = [4,2,5,1,3], target = 3.714286

#     4
#    / \
#   2   5
#  / \
# 1   3

# Output: 4

# redo

def closestValue(root, target):
  min_difference = float('inf')
  val = -1
  while root:
    if min_difference > abs(root.val - target):
      min_difference = abs(root.val - target)
      val = root.val
    if target < root.val:
      root = root.left
    else:
      root = root.right
  return val