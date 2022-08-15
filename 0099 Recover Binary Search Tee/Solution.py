from typing import Optional
from Utilities.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.prev = None
        self.violator1 = None
        self.violator2 = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(node: TreeNode):
            if node is None:
                return

            inorder(node.left)

            if self.prev:
                if not self.violator1:
                    if self.prev.val > node.val:
                        self.violator1 = self.prev
                else:
                    if self.violator1.val < node.val:
                        self.violator2 = self.prev
                        return

            if self.violator2:
                return
            self.prev = node

            inorder(node.right)

        inorder(root)
        if self.violator2 is None:
            self.violator2 = self.prev

        self.violator1.val, self.violator2.val = self.violator2.val, self.violator1.val
