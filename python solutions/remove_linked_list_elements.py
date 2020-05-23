# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode: 
        temp = ListNode()
        temp.next = head
        curr = head
        prev = temp 
        while curr:
            if curr.val == val:
                prev.next = curr.next    
            else:
                prev = curr
            curr = curr.next
        return temp.next