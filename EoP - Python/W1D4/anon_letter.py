# Write a program which takes text for an anonymous letter and text for a magazine and 
# determines if it is possible to write the anonymous letter using the magazine. 
# The anonymous letter can be written using the magazine if for each character in the 
# anonymous letter, the number of times it appears in the anonymous letter is no more 
# than the number of times it appears in the magazine.

# the number of characters that appear in the letter can't be greater than the
# number of characters in the magazine => true
# ex: magazine = "hello" letter = "ehllo" => true
# ex: magazine = "hello" letter = "ehlloo" => false
magazine = "hello" 
letter = "ehlo"

from collections import Counter
def is_letter_constructible_from_magazine(letter, magazine):
  letter_table = Counter(letter)
  magazine_table = Counter(magazine)
  for char in magazine:
    if letter_table[char] > magazine_table[char]:
      return False
  return True

print(is_letter_constructible_from_magazine(letter, magazine))

