# Write a program that takes an array A and an index idx into A 
# and rearranges the elements such that all elements
# less than A[idx] (the pivot) appear first, followed by elements equal to the pivot, 
# followed by elements greater than the pivot

# O(n^2)
def dutch_flag_partition(pivot_index, A):
  pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
  for i in range(len(A)):
    # look for a smaller element
    for j in range(i + 1, len(A)):
      if A[j] < pivot:
        A[i], A[j] = A[j], A[i]
        break
  for i in reversed(range(len(A))):
    if A[i] < pivot:
      break
    # look for a larger element. Stop when we reach an element less than pivot
    # since first pass has moved them to the start of A
    for j in reversed(range(len(A))):
      if A[j] > pivot:
        A[i], A[j] = A[j], A[i]
        break




# O(n)
def dutch_flag_partition(pivot_index, A):
  pivot = A[pivot_index]
  # First pass: group elements smaller than pivot
  smaller = 0
  for i in range(len(A)):
    if A[i] < pivot:
      A[i], A[smaller] = A[smaller], A[i]
      smaller += 1
  # Second pass: group elements larger than pivot
  larger = len(A) - 1
  for i in reversed(len(A)):
    if A[i] < pivot:
      break
    elif A[i] > pivot:
      A[i], A[larger] = A[larger], A[i]
      larger -= 1