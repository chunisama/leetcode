# Write a Program which takes as input an integer array and returns the pair of entries that trap the maximum amount 
# of water.

heights = [2, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]

def get_max_trapped_height(heights):
  left, right, max_water = 0, len(heights) - 1, 0
  while left < right:
    width = right - left
    max_water = max(max_water, width * min(heights[left], heights[right]))
    if heights[left] > heights[right]:
      right -= 1
    else: 
      left += 1
  return max_water

print(get_max_trapped_height(heights))
