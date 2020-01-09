# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        result = []
        while queue and root:
            level = []
            queue_copy = queue[:]
            for item in queue_copy:
                inspect = queue.pop(0)
                if inspect.left != None:
                    queue.append(inspect.left)
                if inspect.right != None:
                    queue.append(inspect.right)
                level.append(item.val)
            result.append(level)
        return result
        
