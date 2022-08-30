from unittest import TestCase
from Solution import Solution
from Utilities.TreeNode import treeNode2List


class TestSolution(TestCase):
    def test_generate_trees1(self):
        x = Solution()
        self.assertEqual(14, len(x.generateTrees(4)))
