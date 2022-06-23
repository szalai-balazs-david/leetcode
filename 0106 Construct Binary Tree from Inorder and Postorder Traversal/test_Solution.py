from unittest import TestCase
from Solution import Solution
from Utilities.TreeNode import treeNode2List


class TestSolution(TestCase):
    def test_buildTree1(self):
        x = Solution()
        expected = [3,9,20,None,None,15,7]
        node = x.buildTree([9,3,15,20,7], [9,15,7,20,3])
        actual = treeNode2List(node)
        self.assertListEqual(expected, actual)

    def test_buildTree2(self):
        x = Solution()
        expected = [-1]
        node = x.buildTree([-1], [-1])
        actual = treeNode2List(node)
        self.assertListEqual(expected, actual)

    def test_buildTree3(self):
        x = Solution()
        expected = [1,2,None]
        node = x.buildTree([2,1], [2,1])
        actual = treeNode2List(node)
        self.assertListEqual(expected, actual)
