# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can 
# see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#     1            <---
#   /   \
#  2     3         <---
#   \     \
#    5     4       <---


#       3            [3]
#      / \
#     4   10
#   /  \
#  2   5


# redo


def rightSideView(root):
  queue = [root]
  level = 1
  num_nodes = 0
  current_level = []
  result = []
  while len(queue): # [3]
    node = queue.pop(0)  # queue = []; node = 3
    current_level.append(node) # CL = [3]
    level -= 1 # lev = 0
    if node.right: 
      queue.append(node.right) # q = [10]
      num_nodes += 1 # NL = 1
    if node.left: 
      queue.append(node.left) # q = [10, 4]
      num_nodes += 1 # NL = 2
    if level == 0:
      result.append(current_level[0].val) # result = [3, 10, 4]
      current_level = []
      level = num_nodes
      num_nodes = 0
  return result

    

