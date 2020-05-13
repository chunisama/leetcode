# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [[root.left, root.right]]
        while stack:
            node = stack.pop()
            if not node[0] and not node[1]:
                continue
            if not node[0] or not node[1]:
                return False
            if node[0].val == node[1].val:
                stack.append([node[0].left, node[1].right])
                stack.append([node[0].right, node[1].left])
            if node[0].val != node[1].val:
                return False
        return True