# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # create a fake node before the original list
        dummy = ListNode(0)
        # attach the dummy node just befor the head, that points to head
        dummy.next= head

        slow= dummy
        fast= dummy
        # move fast pointer n+1 steps
        for _ in range(n+1):
            fast=fast.next
        # move  both pointers until the fast pointer reaches the head
        while fast:
            fast= fast.next
            slow= slow.next
        # remove the nth node
        slow.next = slow.next.next
        
        return dummy.next