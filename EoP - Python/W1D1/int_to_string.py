# Implement an integer to string conversion function, and a string to integer 
# conversison function, For example, if the input to the first function is the 
# integer 314,it should return the string "31.4" and if the input to the second function 
# is the string "314" it should return the integer 314.


# def int_to_string(x):
#   is_negative = False
#   if x < 0:
#     x, is_negative = -x, True
#   s = []
#   while True: 
#     # chr() => parses integers to characters
#     # ord('0') accounting for case when x = 0 
#     # we need to explicitly parse into string since we will break out of interation without a digit if we don't
#     s.append(chr(ord('0') + x % 10))
#     x //= 10
#     if x == 0:
#       break
#   return ('-' if is_negative else '') + ''.join(reversed(s))


# todo string_to_int

# "413" => ["4", "1" ,"3"]
# idx = 0 => 4 * 1
# idx = 1 => 1 * 10
# idx = 2 => 3 * 100
# result += int(arr[idx]) * 10^idx

# def string_to_int(string):
#   result = 0
#   split_str = string.split()
#   for idx, digit in enumerate(split_str):
#     result += int(split_str[idx]) * 10**idx
#   return result

# print(string_to_int("413"))

# [1, 2, 9] => "129" => 129 + 1 = 130 => "130" => ["1", "3", "0"] => [1, 3, 0]
