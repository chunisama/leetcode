# Given two integers and a linked list, reverse sublist between the 
# positions of 2 and 4 within the Linked list

# Ex) () -> 1 -> 2 -> 6 -> 5 -> 8 => 1 -> 5 -> 6 -> 2 -> 8

# have a counter variable to track when i visit the input positions
# dummy node to save the target nodes once i visit them
# traverse the linked list with each step ill increment counter and check if the positions
# are witin the range => then reverse between the positions inclusively


# def reverse_single_sublist(head, start, finish):
#   counter = 0
#   dummy_head = ListNode() 
#   while head.next: 
#     if start <= counter <= finish:
#       prev = dummy_head
#       head.next = prev
#       head = head.next
#     counter += 1
#   return dummy_head.next


def reverse_single_sublist(head, start, finish):
  counter = 0
  dummy_head = ListNode()
  counter2 = finish - start
  while counter < start - 1:
    head = head.next 
    counter += 1

  while counter2 != 0:
    prev = dummy_head
    head.next = prev
    head = head.next
    counter2 -= 1
  return dummy_head