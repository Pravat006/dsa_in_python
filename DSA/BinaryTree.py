# Binary tree

class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

A=TreeNode(1)
B=TreeNode(2)
C=TreeNode(3)
D=TreeNode(4)
E=TreeNode(5)
F=TreeNode(8)

#         1
#     2      3
#   4   5  8

A.left=B
A.right=C
B.left=D
B.right=E
C.left=F

# print(A)#1

# Recursive Pre Order Traversal ( DFS ) , Time: O(n), space: O(n)

def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

# pre_order(A) # 1 2 4 5 3 8

# Recursive In-Order Traversal (DFS) Time: O(n), space: O(n)

def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)

# in_order(A) # 4 2 5 1 8 3

# Recursive Post-Order Traversal (DFS), Time: O(n), Space: O(n)

def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)

# post_order(A) # 4 5 2 8 3 1



# Iterative Pre-Order Traversal (DFS) Time:O(n), Space: O(n)

def pre_order_iterative(node):
    stack = [node]
    while stack:
        node = stack.pop()
        print(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# pre_order_iterative(A)

# Level-Order Traversal (BFS) Time: O(n), Space: O(n)
from collections import deque


def level_order(node):
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        print(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# level_order(A)

#Check if value Exists (DFS) Time: O(n), SPace: O(n)
def search(node, target):
     if not node:
         return False

     if node.val == target:
         return True
     return search(node.left, target) or search(node.right, target)


# res= search(A,8)
# print(res)

# Binary Search Trees (BSTs)

#           5
#        1      8
#      -1  3  7   9

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left, A2.right = B2,C2
B2.left, B2.right = D2,E2
C2.left, C2.right = F2,G2

# print(A2)

# in_order(A2)

# Time: O(log n), Space: O(log n)

def search_bst(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    if target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)

res=search_bst(A2, 1)
print(res)
