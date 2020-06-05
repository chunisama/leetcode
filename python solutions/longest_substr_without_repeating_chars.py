# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        res, left, right = 0, 0, 0
        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                res = max(len(char_set), res)
            else: #s[right] in char_set
                char_set.remove(s[left])
                left += 1
                
        return res