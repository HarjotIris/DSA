from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        remainingSum = targetSum - root.val
        return ((self.hasPathSum(root.left, remainingSum)) or
                 self.hasPathSum(root.right, remainingSum))
    
'''
BFS solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        q = deque([(root, root.val)])
        
        while q:
            node, current_sum = q.popleft()
            
            if not node.left and not node.right:
                if current_sum == targetSum:
                    return True
            
            if node.left:
                q.append((node.left, current_sum + node.left.val))

            if node.right:
                q.append((node.right, current_sum + node.right.val))
        
        return False
'''