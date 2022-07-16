from unittest import TestCase
from Solution import Solution
from Utilities.TreeNode import TreeNode


class TestSolution(TestCase):
    def test_level_order1(self):
        x = Solution()
        tree = TreeNode(3,
                        TreeNode(9),
                        TreeNode(20,
                                 TreeNode(15),
                                 TreeNode(7)))
        expected = [[3],[9,20],[15,7]]
        actual = x.levelOrder(tree)
        self.assertEqual(len(expected), len(actual))
        for i in range(len(expected)):
            self.assertListEqual(expected[i], actual[i])

    def test_level_order2(self):
        x = Solution()
        tree = TreeNode(1)
        expected = [[1]]
        actual = x.levelOrder(tree)
        self.assertEqual(len(expected), len(actual))
        for i in range(len(expected)):
            self.assertListEqual(expected[i], actual[i])

    def test_level_order3(self):
        x = Solution()
        tree = None
        expected = []
        actual = x.levelOrder(tree)
        self.assertEqual(len(expected), len(actual))
        for i in range(len(expected)):
            self.assertListEqual(expected[i], actual[i])
