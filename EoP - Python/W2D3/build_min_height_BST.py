# Given a sorted array, the number of BSTs that can be built on the entries in the array grows enormously with its size. 
# Some of these trees are skewed, and are closer to lists; others are more balanced. 
# See Figure 14.3 on Page 205 for an example.
# How would you build a BST of minimum possible height from a sorted array?

arr = [2, 3, 5, 7, 11, 13, 17, 19, 23]

#      11
#    5   19
#  3  7  17 23 
# 2     13


# assuming we BSTNode Class to create node instances
# O(n)
def build_min_height_bst_sorted_arr(arr):
  if not arr: return None
  middle_idx = (len(arr) - 1) // 2
  root_node = arr[middle_idx]
  left_side = arr[0 : middle_idx]
  right_side = arr[middle_idx + 1]
  left_subtree = build_min_height_bst_sorted_arr(left_side)
  right_subtree = build_min_height_bst_sorted_arr(right_side)
  return BSTNode(root_node, left_subtree, right_subtree)



