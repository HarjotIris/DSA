from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        '''
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
        '''

        queue = deque([root])
        depth = 0
        while queue:
            level = len(queue)
            for _ in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            depth += 1
        return depth