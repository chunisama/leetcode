# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order 
# (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# [1, 2, 3] => 123
                    #  j     
# [6, 2, 1, 5, 4, 3, 0]
# [6, 2, 3, 5, 4, 1, 0] => swapping 1 and 3
# [6, 2, 3, 0, 1, 4, 5] => sort the strictly decreasing area


# def nextPermutation(nums):
#   i = j = len(nums)-1
#   while i > 0 and nums[i-1] >= nums[i]:
#       i -= 1
#   if i == 0:   # nums are in descending order
#       nums.reverse()
#       return
#   print(nums)
  
#   k = i - 1    # find the last "ascending" position
#   while nums[j] <= nums[k]:
#       j -= 1
#   nums[k], nums[j] = nums[j], nums[k]
  
#   print(nums)
#   l, r = k+1, len(nums)-1  # reverse the second part
#   while l < r:
#       nums[l], nums[r] = nums[r], nums[l]
#       l +=1 ; r -= 1
#       print(nums)


