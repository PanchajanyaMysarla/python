"""
Binary Tree Preorder Traversal
Solution
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs.(root,res)
        return res
    
    def dfs(root,res):
        if root:
            res.append(root.val)
            self.dfs(root.left,res)
            self.dfs(root.right,res)
    
    def preorderIteratively(self,root:TreeNode):
        
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
    
        
        