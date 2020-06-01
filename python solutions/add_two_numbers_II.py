# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # traverse l1; create str1
        str1 = ""
        str2 = ""
        while l1:
            str1 = str1 + str(l1.val)
            l1 = l1.next
        while l2:
            str2 = str2 + str(l2.val)
            l2 = l2.next
        temp_int = int(str1) + int(str2)
        temp_arr = list(str(temp_int))
        dummy = ListNode()
        head = dummy
        for num in temp_arr:
            dummy.next = ListNode(int(num))
            dummy = dummy.next
        return head.next