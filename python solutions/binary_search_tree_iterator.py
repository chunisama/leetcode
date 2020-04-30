# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be at least a next smallest number
# in the BST when next() is called.

# redo

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        min_val = self.stack.pop()
        curr_node = min_val.right
        while curr_node:
            self.stack.append(curr_node)
            curr_node = curr_node.left
        return min_val.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
