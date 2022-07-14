from unittest import TestCase
from Solution import Solution
from Utilities.ListNode import createListNode, listNode2list



class TestSolution(TestCase):
    def test_sort_list1(self):
        x = Solution()
        input = createListNode([4,2,1,3])
        result = x.sortList(input)
        actual = listNode2list(result)
        self.assertListEqual([1,2,3,4], actual)

    def test_sort_list2(self):
        x = Solution()
        input = createListNode([-1,5,3,4,0])
        result = x.sortList(input)
        actual = listNode2list(result)
        self.assertListEqual([-1,0,3,4,5], actual)

    def test_sort_list3(self):
        x = Solution()
        input = createListNode([])
        result = x.sortList(input)
        actual = listNode2list(result)
        self.assertListEqual([], actual)
