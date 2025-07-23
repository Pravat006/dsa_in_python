class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


Head= SinglyNode(2)
print("head "+ str(Head))
A= SinglyNode(3)
B= SinglyNode(4)
C= SinglyNode(5)
Head.next= A
A.next= B
B.next= C
# C.next= None
# print(Head)

# Traverse the list -O(n)
curr= Head
while curr:
    # print(curr.next)
    print(curr)
    curr= curr.next

#Dispaly the linked list - O(n)
def display(head):
    currentElement= head
    elements= []
    while currentElement:
        elements.append(str(currentElement.val))
        currentElement= currentElement.next
    print('->'.join(elements))

display(Head)

def search(head,val):
    currentValue= head
    while currentValue:
        if val == currentValue.val:
            print("found at position " + str(currentValue.val))
            return True
        currentValue= currentValue.next
    return False

search(Head,4)











