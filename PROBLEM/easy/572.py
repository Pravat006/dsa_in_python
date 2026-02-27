# 572. Subtree of Another Tree

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        
        # If trees match at current node
        if self.isSame(root, subRoot):
            return True
        
        # Otherwise search left and right
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
    
    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return (self.isSame(p.left, q.left) and
                self.isSame(p.right, q.right))