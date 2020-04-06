# Write a program which takes as input an array of digits encoding a 
# nonnegative decimal integer D and updates the array to represent the integer D + 1. 
# For example, if the input is (1,2,9) then you should update the array to (1,3,0). 
# Your algorithm should work even if it is implemented in a language that has finite-precision arithmetic.

def increment_integer(arr):
  next_int = int(arr.join("")) + 1
  return str(next_int).join("")

# review