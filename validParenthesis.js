// Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
// determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Note that an empty string is also considered valid.

function isValid(s){
  let map = {'(':')', '{':'}', '[': ']'};
  let stack = [];
  if (s.length === 0) return true; 
  for (let i = 0; i < s.length; i++) {
    var char = s[i];
    if (map[char]) {
      stack.push(char);
    } else if (char === ')' || char === '}' || char === ']'){
        if (map[stack.pop()] !== char) {
          return false;
        }
    }
  }
  return stack.length === 0;
}