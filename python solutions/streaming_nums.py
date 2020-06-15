# Design a system that takes in a randomly ordered stream of integers from 1..k. 
# Print numbers in sequential order as they come in. Ex [1,2,4,5,3]

import heapq 
class streamNumbers(object):
  def __init__(self):
    self.heap = []
    self.expected = 1

  def print_curr(self, num):
    if num == self.expected:
      print(num)
      self.expected += 1
    else:
      if self.heap and self.heap[0] == self.expected:
        print(heapq.heappop(self.heap))
        self.expected += 1
      heapq.heappush(self.heap,num)
  
  def print_heap(self):
    print(self.heap)


test = streamNumbers()
test.print_curr(1)
test.print_curr(4)
test.print_curr(3)
test.print_curr(2)
test.print_curr(5)
test.print_curr(8)
test.print_curr(7)
test.print_curr(6)
test.print_curr(9)





test.print_heap()


