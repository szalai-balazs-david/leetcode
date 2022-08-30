from typing import Optional
from Utilities.TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def doStuff(node: Optional[TreeNode]) -> (int, int):
            if node is None:
                return -1000, -1000

            left_max, left_upgoing_max = doStuff(node.left)
            right_max, right_upgoing_max = doStuff(node.right)

            upgoing_max = max(node.val, node.val + left_upgoing_max,
                              node.val + right_upgoing_max)
            local_max = max(upgoing_max, left_max, right_max,
                            node.val + left_upgoing_max + right_upgoing_max)
            return local_max, upgoing_max

        return doStuff(root)[0]
