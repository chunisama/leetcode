# You are given a sequence of adjacent buildings. Each has unit width and an integer height. 
# These buildings form the skyline of a city. 
# An architect wants to know the area of a largest rectangle contained in this skyline. 
# See Figure 17.5 on the next page for an example.
# Let A be an array representing the heights of adjacent buildings of unit width. 
# Design an algorithm to compute the area of the largest rectangle contained in this skyline.

heights = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]

# def compute_largest_rectangle(heights):
#   left, right = 0, len(heights) - 1
#   max_rect, min_height = 0, 0
#   while left <= right:
#     width = right - left + 1
#     min_height = min(heights[left], heights[right])
#     max_rect = max(max_rect, min_height * width) 
#     if heights[left] > heights[right]:
#       right -= 1
#     else:
#       left += 1
#   print(left, right)
#   return max_rect



def compute_largest_rectangle(heights):
  max_area = 0
  for idx in range(len(heights)):
    next = idx + 1
    width = 0
    while heights[idx] > heights[next] and next < len(heights):
      width += 1
      next += 1
      if next == len(heights) - 1:
        break
    curr_area = heights[idx] * width
    max_area = max(max_area, curr_area)
  return max_area
    

print(compute_largest_rectangle(heights))