class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def solver(root):
            if not root:
                return TreeNode(val)
            if val>root.val:
                root.right = solver(root.right)
            else:
                root.left = solver(root.left)
            return root
        return solver(root)