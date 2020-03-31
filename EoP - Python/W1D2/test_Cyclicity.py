# Although a linked list is supposed to be a sequence of nodes ending in null, 
# it is possible to create a cycle in a linked list by making the next field of an element 
# reference to one of the earlier nodes. Write a program that takes the head of a singly 
# linked list and returns null if there does not exist a cycle, and the node at the start 
# of the cycle, if a cycle is present, (You do not know the length of the list in advance.)


# review 
def TestCyclicity(head):
  main_head = head
  visited = {}
  currHead = head
  isCyclicity = False
  while currHead:
    if currHead not in visited:
      visited[currHead] = currHead.next
      currHead = currHead.next
    elif visited[currHead] in visited:
      isCyclicity = True
      break
  if isCyclicity:
    return main_head
  else:
    return None