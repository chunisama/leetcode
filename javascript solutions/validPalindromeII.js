// Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

// Example 1:
// Input: "aba"
// Output: True
// Example 2:
// Input: "abca"
// Output: True
// Explanation: You could delete the character 'c'.


function validPalindrome(s, deleted = 0){
  let left = 0;
  let right = s.length - 1;
  
  while (left < right) {
    if (s[left] === s[right]) {
      left++;
      right--;
      continue;
    }
    
    if (deleted === 1) {
      return false;
    }
    
    return validPalindrome(s.slice(left, right), 1) 
      || validPalindrome(s.slice(left + 1, right + 1), 1);
  }
  
  return true;
}