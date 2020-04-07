# The Collatz conjecture is the following: Take any natural number. If it is odd, triple it 
# and add one; if it is even, halve it. Repeat the process indefinitely. No matter what 
# number you begin with, you will eventually arrive at 1.
# As an example, if we start with 11 we get the sequence 
# 11,34,17,52,26,13,40,20,10,5,16,8,4,2,1. Despite intense efforts, the Collatz conjecture 
# has not been proved or disproved.
# Suppose you were given the task of checking the Collatz conjecture for the first billion 
# integers. A direct approach would be to compute the convergence sequence for each number 
# in this set.
# Test the Collatz conjecture for the first n positive integers.

# review

def test_collatz_conjecture(n):
  verified_nums = set()
  for i in range(3, n + 1):
    sequence = set()
    test_i = i
    while test_i >= i:
      if test_i in sequence:
        return False
      sequence.add(test_i)
      if test_i % 2: 
        if test_i in verified_nums:
          break 
        test_i = 3 * test_i + 1 
      else:
        test_i //= 2 
  return True