from typing import Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        ''' recursive
        result = []
        def pre(node: Optional[TreeNode]):
            if not node:
                return
            
            result.append(node.val)
            pre(node.left)
            pre(node.right)
            

        pre(root)
        return result 
        '''

        # iterative

        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result