# Compute the total number of alpha combinations given a single string of numbers
# input: "1262"
# output: 3
# 1: combo = "azb", 2: combo = "abfb", 3: combo = "lfb"


def decode_variations(num_str, memo = {}):
  one_digit, two_digit = 0, 0
  if len(num_str) == 0:
    return 1
  if num_str in memo:
    return memo[num_str]
  if 1 <= int(num_str[0]) <= 9:
    one_digit = decode_variations(num_str[1:], memo)
  if 10 <= int(num_str[0:2]) <= 26:
    two_digit = decode_variations(num_str[2:], memo)
  memo[num_str] = one_digit + two_digit
  return memo[num_str]

print(decode_variations("1262"))



