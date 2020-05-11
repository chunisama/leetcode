# Given an array nums, write a function to move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n^2)
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         for j in range(i + 1, len(nums)):
        #             if nums[j] != 0:
        #                 nums[i], nums[j] = nums[j], nums[i]
        #                 break
        
        
        # O(n)
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0