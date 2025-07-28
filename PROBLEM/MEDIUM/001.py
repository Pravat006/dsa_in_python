# 2.Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyNode = ListNode(0)
        currentNode = dummyNode
        carry = 0

        while l1 or l2 or carry:
            # Get current values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_num = total % 10

            # Add to result list
            currentNode.next = ListNode(new_num)
            currentNode = currentNode.next

            # Move to next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummyNode.next



