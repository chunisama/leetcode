def search(self, nums: List[int], target: int) -> int:
  low, high = 0, len(nums) - 1
  while low <= high:
    mid = low + (high - low) // 2
    if nums[mid] == target:
      return mid
      # If the left half is sorted and target
      # lies in the left half, go dig into that
      # side. Otherwise, just go right.
    elif nums[low] <= nums[mid]:
      if nums[low] <= target <= nums[mid]:
        high = mid - 1
      else:
        low = mid + 1

      # Else if the right half is sorted and target
      # lies in the right half, go dig into that
      # side. Otherwise, just go left.
    else: # nums[mid] <= nums[high]
      if nums[mid] <= target <= nums[high]:
        low = mid + 1
      else:
        high = mid - 1
  return -1