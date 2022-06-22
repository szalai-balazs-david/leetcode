from Utilities.TreeNode import TreeNode
from typing import Optional


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        if len(preorder) == 2:
            if preorder[0] == inorder[0]:
                return TreeNode(preorder[0], None, TreeNode(preorder[1]))
            else:
                return TreeNode(preorder[0], TreeNode(preorder[1]), None)

        index = inorder.index(preorder[0])
        left_preorder = preorder[1:index + 1]
        left_inorder = inorder[:index]
        right_preorder = preorder[index + 1:]
        right_inorder = inorder[index + 1:]
        root = TreeNode(preorder[0],
                        self.buildTree(left_preorder, left_inorder),
                        self.buildTree(right_preorder, right_inorder))

        return root
