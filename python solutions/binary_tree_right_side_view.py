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



def rightSideView(self, root: TreeNode) -> List[int]:
    result, queue = [], [(root, 0)]
    while queue: 
        curr, level = queue.pop(0)
        if curr:
            if len(result) < level + 1:
                result.append([])
            result[level].append(curr.val)
            queue.append((curr.left, level + 1))
            queue.append((curr.right, level + 1))
    print(result)
    return [x[-1] for x in result]

    

