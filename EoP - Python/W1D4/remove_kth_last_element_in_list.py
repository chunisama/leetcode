# Without knowing the length of a linked list, it is not trivial to delete the kth last element in a singly linked list.
# Given a singly linked list and an integer k, write a program to remove the kth last element from the list. 
# Your algorithm cannot use more than a few words of storage, regardless of the length of the list. 
# In particular, you cannot assume that it is possible to record the length of the list.

# k = 2
# Input: (0) => (1) => (2) => (3) => (4) => null
# Output: (0) => (1) => (2) => (4)
def remove_kth_ele_from_linked_list(head, k):
  slow_pointer = head
  fast_pointer = head
  dummy_head = ListNode()
  dummy_head.next = head
  while k != 0:
    fast_pointer = fast_pointer.next
    k -= 1
  while fast_pointer.next:
    fast_pointer = fast_pointer.next
    slow_pointer = slow_pointer.next
  slow_pointer.next = fast_pointer
  return dummy_head.next
