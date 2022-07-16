from Utilities.TreeNode import TreeNode
from typing import Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        if root.left is None:
            if root.right is None:
                return [root.val]
            return [root.val] + self.inorderTraversal(root.right)

        if root.right is None:
            self.inorderTraversal(root.left) + [root.val]
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
