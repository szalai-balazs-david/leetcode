from unittest import TestCase
from Solution import Solution
from Utilities.ListNode import createListNode, listNode2list


class TestSolution(TestCase):
    def test_reverseKGroup1(self):
        head = createListNode([1,2,3,4,5])

        x = Solution()
        result = x.reverseKGroup(head, 2)

        received = listNode2list(result)
        expected = [2,1,4,3,5]

        self.assertListEqual(expected, received)

    def test_reverseKGroup2(self):
        head = createListNode([1,2,3,4,5])

        x = Solution()
        result = x.reverseKGroup(head, 3)

        received = listNode2list(result)
        expected = [3,2,1,4,5]

        self.assertListEqual(expected, received)

    def test_reverseKGroup3(self):
        head = createListNode([1,2,3,4,5,6,7])

        x = Solution()
        result = x.reverseKGroup(head, 2)

        received = listNode2list(result)
        expected = [2,1,4,3,6,5,7]

        self.assertListEqual(expected, received)

    def test_reverseKGroup4(self):
        head = createListNode([1,2])

        x = Solution()
        result = x.reverseKGroup(head, 2)

        received = listNode2list(result)
        expected = [2,1]

        self.assertListEqual(expected, received)
