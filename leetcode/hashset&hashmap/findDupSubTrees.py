"""
Find Duplicate Subtrees
Solution
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""
#Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    



def findDuplicateSubtrees(self, root):
    count = collections.Counter()
    ans = []
    def collect(node):
        if not node: return "#"
        serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
        count[serial] += 1
        if count[serial] == 2:
            ans.append(node)
        return serial

    collect(root)
    return ans

"""
Approach #2: Unique Identifier [Accepted]
Intuition

Suppose we have a unique identifier for subtrees: two subtrees are the same if and only if they have the same id.

Then, for a node with left child id of x and right child id of y, (node.val, x, y) uniquely determines the tree.

Algorithm

If we have seen the triple (node.val, x, y) before, we can use the identifier we've remembered. Otherwise, we'll create a new one.
class Solution(object):
    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans
        
        Complexity Analysis

Time Complexity: O(N)O(N), where NN is the number of nodes in the tree. We visit each node once.

Space Complexity: O(N)O(N). Every structure we use is using O(1)O(1) storage per node.
"""
