
# Design a stack that supports push, pop, top, and retrieving the minimum element 
# in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []
        self.min = float('inf')
    def push(self, x: int) -> None:
        self.min = min(self.min, x)
        self.val.append([x, self.min])
        
    def pop(self) -> None:
        if len(self.val) > 1:
            res = self.val.pop()
            self.min = self.val[-1][1]
            return res
        else:
            self.min = float('inf')
            return self.val.pop()
    def top(self) -> int:
        return self.val[-1][0]

    def getMin(self) -> int:
        return self.val[-1][1]