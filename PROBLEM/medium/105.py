# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
        index_map= {v:i for i , v in  enumerate(inorder)}
        self.preIdx=0

        def buildTree(left, right):
            if left>right:
                return None

            root_value= preorder[self.preIdx]
            self.preIdx +=1

            root = TreeNode(root_value)
            mid= index_map[root_value]
            root.left= buildTree(left , mid-1)
            root.right= buildTree(mid+1, right)

            return root
        return buildTree(0, len(inorder)-1)