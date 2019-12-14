# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        heap = []
        def helper(root):
            if root != None:
                heapq.heappush(heap, root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return heapq.nsmallest(k, heap)[k-1]
