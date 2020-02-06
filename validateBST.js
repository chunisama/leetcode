// Given a binary tree, determine if it is a valid binary search tree (BST).

// Assume a BST is defined as follows:

// The left subtree of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.

function isValidBSTHelper(node, maxValue = Infinity, minValue = -Infinity) {
  if(node === null) return true;
  
  if(node.val >= maxValue || node.val <= minValue) return false;
  
  const isLeftSubTreeValid  = isValidBSTHelper(node.left,  node.val, minValue);
  const isRightSubTreeValid = isValidBSTHelper(node.right, maxValue, node.val);
  
  return isLeftSubTreeValid && isRightSubTreeValid;
  
}