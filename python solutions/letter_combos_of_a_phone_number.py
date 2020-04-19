# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could 
# represent. A mapping of digit to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_table = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if len(digits) == 0: return []
        def dfs(combination, remaining_digits):
            if len(combination) == 0: 
                combination = [""]
            if len(remaining_digits) == 0: 
                return combination
            digit = remaining_digits.pop(0)
            next_combo = []
            for combo in combination:
                for char in hash_table[digit]:
                    next_combo.append(combo + char)
            return dfs(next_combo, remaining_digits)
        return dfs([],list(digits))