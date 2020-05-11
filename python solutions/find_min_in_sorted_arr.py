# Suppose an array sorted in ascending order is rotated at some pivot unknown to you 
# beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # [3, 4, 5, 1 ,2]
        left, right = 0, len(nums) - 1
        min_val = float('inf')
        if len(nums) == 1: return nums[0]
        if nums[right] > nums[0]: return nums[0]
        while left < right:  
                mid = (left + right)// 2        
                if nums[mid] > nums[mid + 1]:
                    min_val = nums[mid + 1]
                if nums[mid] < nums[mid - 1]:
                    min_val = nums[mid]
                if nums[mid] > nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1
        return min_val