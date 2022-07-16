from Utilities.TreeNode import TreeNode, treeNode2List
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left is not None and not self.isLower(root.left, root.val):
            return False
        if root.right is not None and not self.isHigher(root.right, root.val):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def isLower(self, root: TreeNode, threshold: int) -> bool:
        if root.val >= threshold:
            return False
        if root.left is not None and not self.isLower(root.left, threshold):
            return False
        if root.right is not None and not self.isLower(root.right, threshold):
            return False
        return True

    def isHigher(self, root: TreeNode, threshold: int) -> bool:
        if root.val <= threshold:
            return False
        if root.left is not None and not self.isHigher(root.left, threshold):
            return False
        if root.right is not None and not self.isHigher(root.right, threshold):
            return False
        return True
