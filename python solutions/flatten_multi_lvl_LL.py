# You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

# Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

# Example 1:

# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Explanation:



class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # O(n) iterative
        temp = head
        stack = []
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            elif not head.next and stack:
                head.next = stack.pop()
                head.next.prev = head
            head = head.next
        return temp
                
# O(n) recursive 
#         if not head:
#             return head
#         temp = Node(None, None, head, None)
#         self.flatten_dfs(temp, head)
#         temp.next.prev = None
#         return temp.next
    
#     def flatten_dfs(self, prev, curr):
#         if not curr:
#             return prev
#         curr.prev = prev
#         prev.next = curr

#         tempNext = curr.next
#         tail = self.flatten_dfs(curr, curr.child)
#         print(tail.val)
#         curr.child = None
#         return self.flatten_dfs(tail, tempNext)
        
