from unittest import TestCase
from Solution import Solution
from Utilities.TreeNode import TreeNode, treeNode2List


class TestSolution(TestCase):
    def test_recover_tree1(self):
        x = Solution()
        input = TreeNode(1,
                         TreeNode(3,
                                  None,
                                  TreeNode(2)))
        expected = [3,1,None, None,2]
        x.recoverTree(input)
        actual = treeNode2List(input)
        self.assertListEqual(expected, actual)

    def test_recover_tree2(self):
        x = Solution()
        input = TreeNode(3,
                         TreeNode(1),
                         TreeNode(4,
                                  TreeNode(2)))
        expected = [2,1,4,None, None,3, None]
        x.recoverTree(input)
        actual = treeNode2List(input)
        self.assertListEqual(expected, actual)

    def test_recover_tree3(self):
        x = Solution()
        input = TreeNode(0,
                         TreeNode(1))
        expected = [1,0, None]
        x.recoverTree(input)
        actual = treeNode2List(input)
        self.assertListEqual(expected, actual)

    def test_recover_tree4(self):
        x = Solution()
        input = TreeNode(2,
                         TreeNode(3),
                         TreeNode(1))
        expected = [2,1,3]
        x.recoverTree(input)
        actual = treeNode2List(input)
        self.assertListEqual(expected, actual)
