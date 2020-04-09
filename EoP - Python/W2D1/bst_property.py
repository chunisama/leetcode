# Write a Program that takes as input a binary tree and checks if the tree satisfies 
# the BST property.

# review
def isValidBST(node, lower = float('-inf'), upper = float('inf')):
  if not node: 
    return True
  elif not lower <= node.val <= upper:
    return False
  return isValidBST(node.left, lower, node.val) and isValidBST(node.right, node.val, upper)