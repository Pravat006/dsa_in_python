# 297. Serialize and Deserialize Binary Tree

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue= deque([root])
        res=[]
        while queue:
            node = queue.popleft()

            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        values= data.split(",")

        root= TreeNode(values[0])
        queue= deque([root])

        idx=1
        while queue and idx< len(values):
            node = queue.popleft()

            if values[idx]!="#":
                node.left = TreeNode(int(values[idx]))
                queue.append(node.left)

            idx+=1
            if idx< len(values):
                if values[idx] != "#":
                    node.right= TreeNode(int(values[idx]))
                    queue.append(node.right) 
                idx+=1

        return root        