from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # iterative solution
        '''
        queue = deque()
        queue.append((root.left, root.right))

        while queue:
            t1, t2 = queue.popleft()

            if not t1 and not t2:
                continue

            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True
        '''

        # recursive solution
        def Mirror(t1, t2):
            if not t1 and not t2:
                return True
            
            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            return Mirror(t1.left, t2.right) and Mirror(t1.right, t2.left)
        return Mirror(root.left, root.right)