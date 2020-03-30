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

print(chr(1))