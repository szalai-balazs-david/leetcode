from unittest import TestCase
from Solution import Solution, ListNode


class TestSolution(TestCase):
    def test_merge_two_lists1(self):
        head1 = ListNode(1, ListNode(2, ListNode(4)))
        head2 = ListNode(1, ListNode(3, ListNode(4)))

        x = Solution()
        result = x.mergeTwoLists(head1, head2)

        received = []
        y = result
        while True:
            received.append(y.val)
            if y.next == None:
                break
            else:
                y = y.next
        expected = [1,1,2,3,4,4]

        self.assertListEqual(expected, received)

    def test_merge_two_lists2(self):
        head1 = None
        head2 = None

        x = Solution()
        result = x.mergeTwoLists(head1, head2)

        self.assertIsNone(result)

    def test_merge_two_lists3(self):
        head1 = None
        head2 = ListNode(1)

        x = Solution()
        result = x.mergeTwoLists(head1, head2)

        received = []
        y = result
        while True:
            received.append(y.val)
            if y.next == None:
                break
            else:
                y = y.next
        expected = [1]

        self.assertListEqual(expected, received)
