"""
 Maximum Depth of Binary Tree
Solution
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue
            
        return depth
    

    def maxDepth2(self, root: TreeNode) -> int:
        ans=1
        if not root:
            return 0
        def depth(node,curr=1):
            if not node:
                return 
            if not node.left and not node.right:
                nonlocal ans
                ans=max(ans,curr)
            depth(node.left,curr+1)
            depth(node.right,curr+1)
        depth(root)
        return ans