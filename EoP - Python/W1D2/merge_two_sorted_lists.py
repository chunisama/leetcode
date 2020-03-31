# Consider two singly linked lists in which each node holds a number. 
# Assume the lists are sorted, i.e., numbers in the lists appear in ascending order 
# within each list. The merge of the two lists is a list consisting of the nodes of the 
# two lists in which numbers appear in ascending order.

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
