# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
# The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only 
# if the given words are sorted lexicographicaly in this alien language.

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

def verifying_alien_dictionary(words, order):
  for idx in range(len(words) - 1):
      current_word = words[idx]
      next_word = words[idx + 1]
      idx_2 = 0
      while idx_2 < len(current_word):
          left = current_word[idx_2] if idx_2 < len(current_word) else None
          right = next_word[idx_2] if idx_2 < len(next_word) else None
          if not right:
              return False
          left_idx = order.index(left)
          right_idx = order.index(right)
          if left_idx == right_idx:
              idx_2 += 1
          elif left_idx < right_idx:
              break
          else:
              return False
  return True
    