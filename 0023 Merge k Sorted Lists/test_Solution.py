from unittest import TestCase
from Solution import Solution, ListNode


class TestSolution(TestCase):
    def test_mergeKLists1(self):
        head1 = ListNode(1, ListNode(4, ListNode(5)))
        head2 = ListNode(1, ListNode(3, ListNode(4)))
        head3 = ListNode(2, ListNode(6))

        x = Solution()
        result = x.mergeKLists([head1, head2, head3])

        received = []
        y = result
        while True:
            received.append(y.val)
            if y.next == None:
                break
            else:
                y = y.next
        expected = [1,1,2,3,4,4,5,6]

        self.assertListEqual(expected, received)

    def test_mergeKLists2(self):
        x = Solution()
        result = x.mergeKLists([])

        self.assertIsNone(result)

    def test_mergeKLists3(self):
        x = Solution()
        result = x.mergeKLists([None])

        self.assertIsNone(result)
