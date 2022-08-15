from typing import Optional
from Utilities.TreeNode import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder_traversal(node: TreeNode) -> list[TreeNode]:
            if node is None:
                return []
            result = inorder_traversal(node.left)
            result.append(node)
            result += inorder_traversal(node.right)
            return result

        nodes = inorder_traversal(root)

        violator1 = None
        violator2 = nodes[-1]
        for i in range(len(nodes)):
            if violator1 is None:
                if nodes[i].val > nodes[i+1].val:
                    violator1 = nodes[i]
            else:
                if violator1.val < nodes[i].val:
                    violator2 = nodes[i-1]
                    break
        violator1.val, violator2.val = violator2.val, violator1.val

        return
