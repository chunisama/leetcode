# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
# that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# recursive O(h) worse case o(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # traverse the tree recursively
        if root is p or root is q or not root: 
            return root
        check_left = self.lowestCommonAncestor(root.left,p,q) 
        check_right = self.lowestCommonAncestor(root.right,p,q) 
        if check_left and check_right:
            return root
        return check_left or check_right
    
    