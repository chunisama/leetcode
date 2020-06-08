# Given a string s of '(' , ')' and lowercase English characters. 

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

def minRemoveToMakeValid(s):
  stack = []
  remove_char = []
  for idx, char in enumerate(s):
    if char == "(":
      stack.append(idx)
    elif char == ")":
      if not stack:
        remove_char.append(idx)
      else:
        stack.pop()
    else:
      continue
  
  stack += remove_char
  result = ""
  temp = list(s)
  for idx in stack:
    temp[idx] = "$"

  for char in temp:
    if char != "$":
      result += char

  return result  

print(minRemoveToMakeValid("lee(t(c)o)de)"))