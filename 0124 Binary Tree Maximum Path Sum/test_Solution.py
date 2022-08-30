from unittest import TestCase
from Solution import Solution
from Utilities.TreeNode import TreeNode


class TestSolution(TestCase):
    def test_max_path_sum1(self):
        x = Solution()
        self.assertEqual(6, x.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))))

    def test_max_path_sum2(self):
        x = Solution()
        self.assertEqual(42, x.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

    def test_max_path_sum3(self):
        x = Solution()
        self.assertEqual(-3, x.maxPathSum(TreeNode(-3)))

    def test_max_path_sum4(self):
        x = Solution()
        self.assertEqual(-1, x.maxPathSum(TreeNode(-2, TreeNode(-1))))
