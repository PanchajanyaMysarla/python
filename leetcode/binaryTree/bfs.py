Solution

Binary Tree Level Order Traversalhttps://leetcode.com/problems/binary-tree-level-order-traversal/

Breadh First Search

Using BFS, at any instant only L1 and L1+1 nodes are in the queue.
When we start the while loop, we have L1 nodes in the queue.
for _ in range(len(q)) allows us to dequeue L1 nodes one by one and add L2 children one by one.
Time complexity: O(N). Space Complexity: O(N)
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q, result = deque(), []
        if root:
            q.append(root)
        while len(q):
            level = []
            for _ in range(len(q)):
                x = q.popleft()
                level.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            result.append(level)
        return result
Depth First Search

Use a variable to track level in the tree and use simple Pre-Order traversal
Add sub-lists to result as we move down the levels
Time Complexity: O(N)
Space Complexity: O(N) + O(h) for stack space
class Solution(object):
    def levelOrder(self, root):
        result = []
        self.helper(root, 0, result)
        return result
    
    def helper(self, root, level, result):
        if root is None:
            return
        if len(result) <= level:
            result.append([])
        result[level].append(root.val)
        self.helper(root.left, level+1, result)
        self.helper(root.right, level+1, result)
        
        
        
        
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.bfs(root,0,res)
        return res
        
    def bfs(self,root,level,res):
        if root:
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            self.bfs(root.left,level+1,res)
            self.bfs(root.right,level+1,res)
            
            
        
        