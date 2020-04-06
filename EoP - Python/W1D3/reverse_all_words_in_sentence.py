# Given a string containing a set of words separated by whitespace, we would like to transform it to a string 
# in which the words appear in the reverse order. For example, "Alice likes Bob" transforms to "Bob likes Alice".
# We do not need to keep the original string. Implement a function for reversing the words in a string s.


# ex: "Alice likes Bob" => "Bob likes Alice"

# naive approach
def reverse_all_words_in_sentence(sentence):
  words = sentence.split(" ")
  reversed_words = list(reversed(words))
  # words.reverse()
  # print(reversed_words)
  return " ".join(reversed_words)

print(reverse_all_words_in_sentence('Alice likes Bob'))