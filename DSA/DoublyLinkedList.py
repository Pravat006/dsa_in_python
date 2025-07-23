#Doubly linked list

class DoublyNode:
    def __init__(self,val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.val)

head =tail= DoublyNode(8)
# print(head)
# print(tail)

#Display elements in ll - O(n)
def display(head):
    currentVal= head
    elements= []
    while currentVal:
        elements.append(str(currentVal.val))
        currentVal = currentVal.next
    print('<->'.join(elements))

# display(head)

#insert at beginning - O(n)
def insert_at_beginning(head,tail,val):
    new_node= DoublyNode(val, next= head)
    # print("new_node",new_node)
    # print("hea prev",head)
    head.prev= new_node
    return new_node , tail

head, tail = insert_at_beginning(head,tail,3)
head, tail = insert_at_beginning(head,tail,5)
display(head)
display(tail)


#insert at end - O(n)
def insert_at_end(head,tail,val):
    new_node= DoublyNode(val, prev= tail)
    # print("new_node",new_node)
    # print("hea prev",head)
    tail.next= new_node
    return new_node , head
head, tail = insert_at_end(head,tail,6)
display(head)
display(tail)