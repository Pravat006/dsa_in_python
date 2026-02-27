# 100. Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if(p==None and q==None):
            return True
        elif(p==None or q==None):
            return False
        elif(p.val != q.val):
            return False
        return self.isSameTree(p.left , q.left) and self.isSameTree(p.right, q.right)