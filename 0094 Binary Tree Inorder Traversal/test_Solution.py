from unittest import TestCase
from Solution import Solution
from Utilities.TreeNode import TreeNode, treeNode2List


class TestSolution(TestCase):
    def test_inorder_traversal1(self):
        x = Solution()
        tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertListEqual([1,3,2], x.inorderTraversal(tree))

    def test_inorder_traversal2(self):
        x = Solution()
        tree = None
        self.assertListEqual([], x.inorderTraversal(tree))

    def test_inorder_traversal3(self):
        x = Solution()
        tree = TreeNode(1)
        self.assertListEqual([1], x.inorderTraversal(tree))
