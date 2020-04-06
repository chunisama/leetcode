# implement a stack that have these operations

# max operation => return the max val stored in the stack
# push operation => appending to the top of the stack => i.e (in an array elements will be added to the end)
# pop operation => removing of the bottom of the stack => i.e (in an array elements will be removed from the end)

# review
class Stack:
  def __init__ (self):
    self.stack = []
    self.max_val = 0 # => or Infinity if we are considering negative numbers

  def push_val(self, data):
    # data = {
    #   val : 5,
    #   max : val if val > self.max_val else self.max_val
    # }
    entry = {}
    entry["val"] = data
    entry["max"] = data if data > self.max_val else self.max_val
    self.stack.insert(0, entry)
  
  def pop_val(self):
    # pop() removes from the end 
    self.stack.pop()

  def max(self):
    # naive approach O(n)
    # return max(self.stack)
    
    # efficient approach O(1)
    return self.stack[-1]["max"]


  
