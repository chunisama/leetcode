# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0
        stack = [root]
        if not root:
            return 0
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                if not node.left.left and not node.left.right:
                    total += node.left.val
            if node.right:
                stack.append(node.right)
        return total
