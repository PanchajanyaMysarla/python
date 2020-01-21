"""
Binary Tree Inorder Traversal
Solution
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=  []
        self.dfs(root,res)
        return res
    def dfs(self,root,res):
        if root:
            self.dfs(root.left,res)
            res.append(root.val)
            self.dfs(root.right,res)
        
    def iterative(self,root):
        res= []
        stack = []
        curr = root
        
        while curr or len(stack) != 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
        
        