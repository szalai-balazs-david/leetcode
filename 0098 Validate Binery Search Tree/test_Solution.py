from unittest import TestCase
from Solution import Solution
from Utilities.TreeNode import TreeNode


class TestSolution(TestCase):
    def test_is_valid_bst1(self):
        x = Solution()
        tree = TreeNode(2,
                        TreeNode(1),
                        TreeNode(3))
        self.assertEqual(True, x.isValidBST(tree))

    def test_is_valid_bst2(self):
        x = Solution()
        tree = TreeNode(5,
                        TreeNode(1),
                        TreeNode(4,
                                 TreeNode(3),
                                 TreeNode(6)))
        self.assertEqual(False, x.isValidBST(tree))

    def test_is_valid_bst3(self):
        x = Solution()
        tree = TreeNode(5,
                        TreeNode(4),
                        TreeNode(6,
                                 TreeNode(3),
                                 TreeNode(7)))
        self.assertEqual(False, x.isValidBST(tree))
