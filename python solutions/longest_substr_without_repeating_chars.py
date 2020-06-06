# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# sub_str_set = [a,b,c]
# max_substr_length = max(len(sub_str_set, max_substr_length)
#         1
# Input: "a b c a b c b b"
#             2

# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
  sub_str_set = set()
  result, left, right = 0, 0, 0
  while right < len(s):
    if s[right] not in sub_str_set:
      sub_str_set.add(s[right])
      right += 1
      result = max(len(sub_str_set), result)
    else: # s[right] inside my sub_str_set
      sub_str_set.remove(s[left])
      left += 1
  return result

print(lengthOfLongestSubstring('abcabcbb'))