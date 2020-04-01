# Consider a coordinate system for the Milky Way, in which Earth is at (0,0,0). 
# Model stars as points, and assume distances are in light years. The Milky Way consists 
# of approximately 1012 stars, and their coordinates are stored in a file.
# How would you compute the k stars which are closest to Earth?

import heapq 
# import heappop, heappush

# review
def findKthSmallestStars(stars, k):
  max_heap = []
  for star in stars:
    totalDistance = sum(star)
    heapq.heappush(max_heap, -totalDistance)
    if len(max_heap) == k + 1:
      heapq.heappop(max_heap)
  return max_heap.sort() 