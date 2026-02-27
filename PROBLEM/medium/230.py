# 230. Kth Smallest Element in a BST

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.k=k
        self.result =None
        def inOrder(node):
            if not node or self.result is not None:
                return
            
            inOrder(node.left)
            self.k -=1
            if self.k==0:
                self.result= node.val
            
            inOrder(node.right)
        inOrder(root)
        return self.result
