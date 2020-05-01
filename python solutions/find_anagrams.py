
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:    
        # "abc"    
        # "cbaebabacd"
        left, right = 0, len(p) - 1
        counter_p = Counter(p)
        counter_s = Counter(s[left:right + 1])
        result = []
        while left < len(s) - len(p):
            if counter_s == counter_p:
                result.append(left)
            counter_s[s[left]] -= 1
            if counter_s[s[left]] == 0:
                counter_s.pop(s[left])       
            left += 1
            right += 1
            if s[right] in counter_s:
                counter_s[s[right]] += 1
            else:
                counter_s[s[right]] = 1
        if counter_s == counter_p:
            result.append(left)
        return result