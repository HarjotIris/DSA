class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root is None:
        return []
    
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Example Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inorder_traversal(root))  # Output: [4, 2, 5, 1, 3]
