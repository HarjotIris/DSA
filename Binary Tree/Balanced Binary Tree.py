from typing import Optional
# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checknode(node):
            if not node:
                return 0
            
            left = checknode(node.left)
            right = checknode(node.right)

            

            if left == -1:
                return -1
            
            if right == -1:
                return -1
            
            if abs(left - right)>1:
                return -1
            
            return max(left, right) + 1
        
        return checknode(root) != -1