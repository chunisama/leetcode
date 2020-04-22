# Design an algorithm that takes as input a BST and two nodes, and returns the LCA of the two nodes. 
# For example, for the BST in Figure 14.L on Page 198, and nodes C and G,your algorithm should return B. 
# Assume all keys are distinct. Nodes do not have references to their parents.

# redo

def find_LCA_BST(tree, node_a, node_b):
  while tree.data < node_a.data and tree.data > node_b.data:
    # keep searching since tree is outside of [node_a, node_b]
    while tree.data < node_a.data:
      tree = tree.right # LCA must be the right child
    while tree.data > node_b.data:
      tree = tree.left # LCA must bet the left child
  # now node_a.data <= tree.data and tree.data <= node_b.data
  return tree