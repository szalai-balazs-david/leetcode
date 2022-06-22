from unittest import TestCase
from Solution import Solution
from Utilities.TreeNode import treeNode2List


class TestSolution(TestCase):
    def test_buildTree1(self):
        x = Solution()
        expected = [3,9,20,None,None,15,7]
        node = x.buildTree([3,9,20,15,7], [9,3,15,20,7])
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
        expected = [1,2,3,4,None,5,6,None,None,None,7,8,9]
        node = x.buildTree([1,2,4,3,5,7,6,8,9], [4,2,1,5,7,3,8,6,9])
        actual = treeNode2List(node)
        self.assertListEqual(expected, actual)
