from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        # BFS solution - iterative

        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue # both are none

            if not node1 or not node2:
                return False # one is none, one isn't
            
            if node1.val != node2.val:
                return False 
            # adding the children to the in the same order
            queue.append((node1.left, node2.left)) 
            queue.append((node1.right, node2.right))

        return True
        '''

        # recursive solution - DFS
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)