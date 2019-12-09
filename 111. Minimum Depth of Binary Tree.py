# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            x = self.minDepth(root.right) + 1
            y = self.minDepth(root.left) + 1
            if x == 1 and y != 1:
                return y
            elif x != 1 and y == 1:
                return x
            else:
                return min(x, y)
