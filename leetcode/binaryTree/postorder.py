"""
Binary Tree Postorder Traversal
Solution
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root,res)
        return res
    def helper(self,root,res):
        if root:
            self.helper(root.left,res)
            self.helper(root.right,res)
            res.append(root.val)
            
    
    def iterativepostorder(self,root):
        res = []
        stack = [root]
        res2 = collections.deque()
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                res2.appendleft(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res2,res[::-1]
        
        
        
        
        
        
        
        
        