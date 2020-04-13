# A BST is a sorted data structure, which suggests that it should be possible to find the k largest keys easily.
# Write a program that takes as input a BST and an integer k, and returns the k largest elements in the BST in 
# decreasing order. For example, if the input is the BST in Figure 14.1 on Page 198 and k = 3, 
# your program should return [53,47,43].

#         10
#       /    \
#      7     15
#     / \    /
#    5   8  12
  
# k = 3
# [10, 12, 15]


# O(h)
def find_kth_largest_BST(root, k):
  kth_largest = []
  def build_tree(root):
    if root and len(kth_largest) < k:
      build_tree(root.right)
      if len(kth_largest) < k:
        kth_largest.append(root.value)
        build_tree(root.left)
  build_tree(root)
  return kth_largest
  