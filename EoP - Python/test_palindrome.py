# For the purpose of this problem, define a palindromic string to be a string 
# which when all the nonalphanumeric are removed it reads the same front to back ignoring 
# case. For example, "A man, a plan, a canal/ Panama." and "Able was I, ere I saw Elba!" 
# are palindromic, but "Ray a Ray" is not.
# Implement a function which takes as input a string s and 
# returns true if s is a palindromic string.


def test_palindrome(words):
  left, right = 0, len(words) - 1
  while left < right:
    if not words[left].isalnum():
      left += 1
    elif not words[right].isalnum():
      right -= 1
    elif words[left] != words[right]:
      return False
    else:
      left += 1
      right -= 1
  return True
print(test_palindrome("a man a plan a canal panama")) # => true
print(test_palindrome("ray a ray")) # => false