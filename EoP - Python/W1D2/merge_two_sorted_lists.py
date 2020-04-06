# Consider two singly linked lists in which each node holds a number. 
# Assume the lists are sorted, i.e., numbers in the lists appear in ascending order 
# within each list. The merge of the two lists is a list consisting of the nodes of the 
# two lists in which numbers appear in ascending order.

# pointer 1
                      # 1
# (1) => (3) => (5) => null

# pointer 2
              #  2
# (2) => (4) => (6)

# building output
# (m) => (1)  #=> (2) => (3) => (4) => (5)  

# output
# (1) => (2) => (3) => (4) => (5) => (6)

# attempt 2
def merged_LL(L1, L2):
  merged = ListNode()
  merged_dummy_head = merged
  pointer_1 = L1
  pointer_2 = L2
  while pointer_1 and pointer_2:
    if pointer_1.val < pointer_2.val:
      merged.next = pointer_1
      merged = merged.next
      pointer_1 = pointer_1.next 
    else:
      merged.next = pointer_2
      merged = merged.next
      pointer_2 = pointer_2.next
  merged.next = pointer_1 or pointer_2
  return merged_dummy_head.next

def merge_two_sorted_lists(L1, L2):
  # creates a placeholder for the merged list
  dummy_head = ListNode()
  tail = ListNode()

  while L1 and L2:
    if L1.data < L2.data:
      tail.next = L1
      L1 = L1.next 
    else:
      tail.next = L2
      L2 = L2.next
    tail = tail.next
  
  # appends the remaining nodes of L1 or L2
  tail.next = L1 or L2
  return dummy_head.next
