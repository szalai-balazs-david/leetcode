from unittest import TestCase
from Solution import Solution
from Utilities.TreeNode import TreeNode, treeNode2List


class TestSolution(TestCase):
    def test_sorted_array_to_bst1(self):
        x = Solution()
        input = [-10,-3,0,5,9]
        expected = [0,-3,9,-10,None,5, None]
        actual = x.sortedArrayToBST(input)
        self.assertListEqual(expected, treeNode2List(actual))

    def test_sorted_array_to_bst2(self):
        x = Solution()
        input = [1,3]
        expected = [3,1, None]
        actual = x.sortedArrayToBST(input)
        self.assertListEqual(expected, treeNode2List(actual))
