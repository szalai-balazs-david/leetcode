from Utilities.TreeNode import TreeNode
from typing import Optional


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        match len(inorder):
            case 0:
                return None
            case 1:
                return TreeNode(inorder[0])
            case 2:
                if inorder[0] == postorder[0]:
                    return TreeNode(inorder[1], TreeNode(inorder[0], None))
                return TreeNode(inorder[0], None, TreeNode(inorder[1]))

        i = inorder.index(postorder[-1])

        return TreeNode(postorder[-1],
                        self.buildTree(inorder[:i], postorder[:i]),
                        self.buildTree(inorder[i + 1:], postorder[i: -1]))
