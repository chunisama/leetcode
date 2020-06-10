# Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.
# Example 1:

# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation: 
# The first missing number is 5.
# Example 2:

# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation: 
# The missing numbers are [5,6,8,...], hence the third missing number is 8.
# Example 3:

# Input: A = [1,2,4], K = 3
# Output: 6
# Explanation: 
# The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def num_missing(idx):
            return nums[idx] - nums[0] - idx
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if num_missing(mid) < k:
                left = mid + 1
            else:
                right = mid
        return nums[left - 1] + k - num_missing(left - 1)