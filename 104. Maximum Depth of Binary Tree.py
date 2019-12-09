# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            x = self.maxDepth(root.left) + 1
            y = self.maxDepth(root.right) + 1
            return max(x, y)
