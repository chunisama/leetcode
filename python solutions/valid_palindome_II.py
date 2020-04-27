# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

def validPalindrome(self, s: str) -> bool:
    def reverse(str):
        temp = list(str)
        temp.reverse()
        return "".join(temp)
    if reverse(s) == s:
        return True
    else:
        left, right = 0, len(s) - 1
        temp = list(s)
        while left < right:
            if temp[left] != temp[right]:
                delete_right = temp[:]
                delete_right.pop(right)
                temp.pop(left)
                delete_left = temp
                break
            else:
                right -= 1
                left += 1
        version_1 = "".join(delete_left)
        version_2 = "".join(delete_right)
        return reverse(version_1) == version_1 or reverse(version_2) == version_2