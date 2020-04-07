# Write a program that takes as input a BST and a value, and returns the first key that would 
# appear in an inorder traversal which is greater than the input value. For example, when 
# applied to the BST in Figure 14.1 on Page 198 you should retum 29 for input 23.


#       (20)
#      /    \
#     15    30
#    /  \   / \
#   10  17 25  35

# input: root, key = 32

def find_greater_node_than_key(root, key):
  if not root: return None
  if root.val > key:
    return root
  elif root.val <= key:
    return find_greater_node_than_key(root.right, key)


