# Given two nodes in a binary tree, design an algorithm that computes their LCA.
# Assume that each node has a parent pointer.

#       a
#      / \
#     b   c
#    / \   \
#   d   e   f

# edge case: can't compare nodes pointing to each other
# nodes => d, f 
# LCA = a => a parent node that both nodes share 

# nodes = d, c
# root_node = a
# hash_table = {
  # a : [b, c],
  # b : [d, e],
  # c : f
  # d : None,
  # e : None,
  # f : None
# }

# nodes = d, e
# hash_table = {
  # d : b,
  # e : b,
# }

# iterative solution
def search_LCA(node_1, node_2, root):
  path_to_root = []
  while node_1:
    path_to_root.append(node_1)
    node_1 = node_1.parent
  while node_2:
    if node_2 in path_to_root: return node_2.parent
    node_2 = node_2.parent

# recursive solution
def search_LCA(node_1, node_2, root):
  if root is node_1 or root is node_2 or not root:
    return root
  left = search_LCA(node_1, node_2, root.left)
  right = search_LCA(node_1, node_2, root.right)
  if left and right:
    return root
  return left or right

# todo : watch video