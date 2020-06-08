# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]

# recursively
def preorderTraversal1(root):
  def dfs(root, result):
    if root:
      result.append(root.val)
      dfs(root.left, result)
      dfs(root.right, result)
  result = []
  dfs(root, result)
  return result

# iterative
def preorderTraversal2(root):
  stack, result = [root], []
  while stack:
    node = stack.pop()
    if node:
      result.append(node.val)
      stack.append(node.right)
      stack.append(node.left)
  return result