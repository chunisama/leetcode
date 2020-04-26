# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:

# Each element in the result must be unique.
# The result can be in any order.


# O(n x m)
# def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#   result = []
#   unique_pool = set(nums1)
#   for num in nums2:
#     if num in unique_pool:
#       result.append(num)
#       unique_pool.remove(num)
#   return result

#                             1                1
# Input:
# Output: [2,3]
# Duplicates, negative values, single value lists, 0's, and empty list arguments.
# Other considerations might include
# sparse arrays.
# O(n) time, O(1) space will not consider the result into its calculation
def intersection(nums1, nums2):
  first_pointer = 0
  second_pointer = 0
  result = []
  while first_pointer < len(nums1) and second_pointer < len(nums2):
    if nums1[first_pointer] == nums2[second_pointer]:
      result.append(nums1[first_pointer])
      first_pointer += 1
      # print(first_pointer, second_pointer)
      if nums1[first_pointer] != nums2[second_pointer]:
        second_pointer += 1
    else:
      if first_pointer != len(nums1) - 1:
        first_pointer += 1
      else:
        continue
  return result

                    # 1
nums_1 = [1,1,1,1,2,2,3,4]
          # 1
nums_2 = [2,4]
print(intersection(nums_1, nums_2))