# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:

# Input: "race a car"
# Output: false

def valid_palindrome(s):
  left, right = 0, len(s) - 1
  while left < right:
    print(s[left], s[right])
    if not s[left].isalnum():
      left += 1
    elif not s[right].isalnum():
      right -= 1
    elif s[left].lower() != s[right].lower():
      return False
    else:
      left += 1
      right -= 1
  return True
print(valid_palindrome("A man, a plan, a canal: Panama"))
