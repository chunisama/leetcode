# Given the array = ["all", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
# find the shortest distance between a pair of words
# i.e "no" the shortest distance between "no", "work", "no"

#                                                              1            2 
arr = ["all", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
# dict = {all:0, work:1, and:2, no:3 }

# O(n), O(m = # of unique words in the arr)
def find_nearest_repeated_entries_in_arr(arr):
  hash_table = {}
  min_distance = float("inf")
  for curr_idx, word in enumerate(arr):
    if word not in hash_table:
      hash_table[word] = curr_idx
    else:
      min_distance = min(min_distance, curr_idx - hash_table[word])
      hash_table[word] = curr_idx
  return min_distance


print(find_nearest_repeated_entries_in_arr(arr))