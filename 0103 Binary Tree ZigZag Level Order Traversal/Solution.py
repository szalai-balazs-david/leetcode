from typing import Optional
from Utilities.TreeNode import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        results = []
        current = [root]
        reverse = False

        while len(current) != 0:
            next_set = []
            sub_result = []
            for node in current:
                sub_result.append(node.val)
                if node.left:
                    next_set.append(node.left)
                if node.right:
                    next_set.append(node.right)
            if reverse:
                sub_result.reverse()
            results.append(sub_result)
            current = next_set
            reverse = not reverse

        return results
