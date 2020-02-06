# Given a non-empty, singly linked list with head node head, 
# return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

def middleNode(self, head: ListNode) -> ListNode:
  tmp = head
  while tmp and tmp.next:
    head = head.next
    tmp = tmp.next.next
  return head