# Manyy algorithms require as a subroutine the computation of the kth largest element of an array. 
# The first largest element is simply the largest element. The nth largest element is the 
# smallest element, where n is the length of the array,
# For example, if the input array I = [3,2,1,5,4], then A[3] is the first largest element in A,
# A[0] is the third largest element in A, and A[2] is the fifth largest element in A.
# Design an algorithm for computing the kth largest element in an array.

# arr = [3, 2, 1, 5, 4], k = 1 => 5
# arr = [3, 2, 1, 5, 4], k = 2 => 4
# arr = [3, 2, 1, 5, 4], k = 3 => 3

# brute force => o(nlogn)
# def find_the_kth_largest_ele(arr, k):
#   sorted_arr = sorted(arr, reverse = True)
#   return sorted_arr[k - 1]


# todo

# faster heap approach => ???? time complexity
import heapq
def find_the_kth_largest_ele(arr, k):
  max_heap = []
  i = 1
  for num in arr:
    heapq.heappush(max_heap, -num)
  while i <= k:
    if i == k: 
      return heapq.heappop(max_heap) * -1
    else:
      heapq.heappop(max_heap)
    i += 1
  
print(find_the_kth_largest_ele([3, 2, 1, 5, 4], 1))
