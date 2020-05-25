# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        res = 0
        x = abs(x)
        while x: #1
            res = res * 10 + (x % 10) # 20 + 1
            x = x//10 # 1
        if res > (2**31)-1 or res < -2**31:
            return 0
        return res * sign
         