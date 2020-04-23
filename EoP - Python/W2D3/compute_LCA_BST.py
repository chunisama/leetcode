# Design an algorithm that takes as input a BST and two nodes, and returns the LCA of the two nodes. 
# For example, for the BST in Figure 14.L on Page 198, and nodes C and G,your algorithm should return B. 
# Assume all keys are distinct. Nodes do not have references to their parents.

# redo
# O(h) => height of the BST

# iterative
def find_LCA_BST(root, node_a, node_b):
  while root.data < node_a.data or root.data > node_b.data:
    # keep searching since root is outside of [node_a, node_b]
    while root.data < node_a.data:
      root = root.right # LCA must be the right child
    while root.data > node_b.data:
      root = root.left # LCA must bet the left child
  # now node_a.data <= root.data and root.data <= node_b.data
  return root

# recursive
def find_LCA_BST(root, node_1, node_2):
  if root > max(node_1.data, node_2.data):
    # check left child
    return find_LCA_BST(root.left, node_1, node_2)
  elif root < min(node_1.data, node_2.data):
    # check right child
    return find_LCA_BST(root.right, node_1, node_2)
    # found LCA since our current node will be less than node 2, and greater than node 1
  else:
    return root