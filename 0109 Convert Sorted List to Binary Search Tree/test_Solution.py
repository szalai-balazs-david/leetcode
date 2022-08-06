from unittest import TestCase
from Utilities.ListNode import createListNode, ListNode
from Utilities.TreeNode import treeNode2List
from Solution import Solution


class TestSolution(TestCase):
    def test_sorted_list_to_bst1(self):
        x = Solution()
        input = createListNode([-10,-3,0,5,9])
        expected = [0,-3,9,-10,None,5, None]
        actual = treeNode2List(x.sortedListToBST(input))
        self.assertListEqual(expected, actual)

    def test_sorted_list_to_bst2(self):
        x = Solution()
        expected = []
        actual = treeNode2List(x.sortedListToBST(None))
        self.assertListEqual(expected, actual)
