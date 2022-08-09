from unittest import TestCase
from Solution import Solution
from Utilities.ListNode import listNode2list, createListNode


class TestSolution(TestCase):
    def test_rotate_right1(self):
        x = Solution()
        expected = [4,5,1,2,3]
        input = createListNode([1,2,3,4,5])
        result = x.rotateRight(input, 2)
        actual = listNode2list(result)
        self.assertListEqual(expected, actual)

    def test_rotate_right2(self):
        x = Solution()
        expected = [2,0,1]
        input = createListNode([0,1,2])
        result = x.rotateRight(input, 4)
        actual = listNode2list(result)
        self.assertListEqual(expected, actual)

    def test_rotate_right3(self):
        x = Solution()
        expected = [1]
        input = createListNode([1])
        result = x.rotateRight(input, 1)
        actual = listNode2list(result)
        self.assertListEqual(expected, actual)

    def test_rotate_right4(self):
        x = Solution()
        expected = [1,2]
        input = createListNode([1,2])
        result = x.rotateRight(input, 2)
        actual = listNode2list(result)
        self.assertListEqual(expected, actual)
