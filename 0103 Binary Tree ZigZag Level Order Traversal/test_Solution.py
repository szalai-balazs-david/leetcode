from unittest import TestCase
from Solution import Solution
from Utilities.TreeNode import TreeNode

class TestSolution(TestCase):
    def test_zigzag_level_order1(self):
        x = Solution()
        input = TreeNode(3,
                         TreeNode(9),
                         TreeNode(20,
                                  TreeNode(15),
                                  TreeNode(7)))
        expected = [[3],[20,9],[15,7]]
        actual = x.zigzagLevelOrder(input)
        self.assertListEqual(expected, actual)

    def test_zigzag_level_order2(self):
        x = Solution()
        input = TreeNode(1)
        expected = [[1]]
        actual = x.zigzagLevelOrder(input)
        self.assertListEqual(expected, actual)

    def test_zigzag_level_order3(self):
        x = Solution()
        input = None
        expected = []
        actual = x.zigzagLevelOrder(input)
        self.assertListEqual(expected, actual)
