# 23. Merge k Sorted Lists
'''
1.create an heap(array)
2. push first node of each list into heap
        HEAP, INDEX, NODE
3.create a dummy result node
4.Process heap
    -pop the smallest node from the heap
    -add smallest node to the result
    -if next node of the current node exist then push it to heap
5. return the desult list

'''


import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap=[]
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        result=ListNode(0)
        curr=result

        while heap:
            val, i, node =heapq.heappop(heap)
            curr.next=node
            curr= curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return result.next
