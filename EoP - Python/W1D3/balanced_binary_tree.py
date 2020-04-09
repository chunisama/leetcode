# Write a program that takes as input the root of a binary tree and 
# checks whether the tree is height- balanced.

# watch alvin's explanation for this
#     (10)
#     /  \
#    5    20
#   / \   / \
#  1   8  15 35
 
# O(n)
def is_balanced(root):
  def get_height(root):
    if not root: return -1
    return 1 + max(get_height(root.left), get_height(root.right))
  
  if not root: return True
  height_difference = abs(get_height(root.left) - get_height(root.right)) <= 1
  return height_difference and is_balanced(root.left) and is_balanced(root.right)
  