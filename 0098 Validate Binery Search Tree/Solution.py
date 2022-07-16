from Utilities.TreeNode import TreeNode, treeNode2List
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.isWithin(root, None, None)

    def isWithin(self, root: TreeNode, low: Optional[int], high: Optional[int]) -> bool:
        if low is not None and root.val <= low:
            return False
        if high is not None and root.val >= high:
            return False

        if root.left is not None and not self.isWithin(root.left, low, root.val):
            return False
        if root.right is not None and not self.isWithin(root.right, root.val, high):
            return False
        return True
