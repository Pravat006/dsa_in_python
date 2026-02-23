# 143. Reorder List

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        first=head
        slow= head
        fast=head
        
        # move t\the fast and slow pointer until fast reached end
        while fast and fast.next !=None:
            slow= slow.next
            fast=fast.next.next
        

        #  reverse the seconds half sarting from slow.next
        # split the 1st half 
        prev=None
        nxt=None
        cur= slow.next
        slow.next=None
        while cur:
            nxt=cur.next
            cur.next= prev
            prev=cur
            cur=nxt


        # merge wto halves alternately
        first=head
        second=prev
        while second:
            temp1=first.next
            temp2= second.next

            first.next=second
            second.next= temp1

            first= temp1
            second=temp2