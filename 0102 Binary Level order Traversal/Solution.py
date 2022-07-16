from Utilities.TreeNode import TreeNode
from typing import Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        elements = [root]
        result = []
        while len(elements) > 0:
            children = []
            level = []

            for element in elements:
                level.append(element.val)
                if element.left is not None:
                    children.append(element.left)
                if element.right is not None:
                    children.append(element.right)

            result.append(level)
            elements = children

        return result
