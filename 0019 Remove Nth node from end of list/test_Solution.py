from unittest import TestCase
from Solution import Solution, ListNode


class TestSolution(TestCase):
    def test_removeNthFromEnd1(self):
        head = ListNode()
        head.val = 1
        previous = head
        for i in range(4):
            previous.next = ListNode()
            previous = previous.next
            previous.val = i + 2

        x = Solution()
        result = x.removeNthFromEnd(head, 2)

        self.assertEqual(1, result.val)
        next = result.next
        self.assertEqual(2, next.val)
        next = next.next
        self.assertEqual(3, next.val)
        next = next.next
        self.assertEqual(5, next.val)
        next = next.next
        self.assertIsNone(next)

    def test_removeNthFromEnd2(self):
        head = ListNode()
        head.val = 1

        x = Solution()
        result = x.removeNthFromEnd(head, 1)

        self.assertIsNone(result)

    def test_removeNthFromEnd3(self):
        head = ListNode()
        head.val = 1
        head.next = ListNode()
        child = head.next
        child.val = 2

        x = Solution()
        result = x.removeNthFromEnd(head, 1)

        self.assertEqual(1, result.val)
        next = result.next
        self.assertIsNone(next)

    def test_removeNthFromEnd4(self):
        head = ListNode()
        head.val = 1
        head.next = ListNode()
        child = head.next
        child.val = 2

        x = Solution()
        result = x.removeNthFromEnd(head, 2)

        self.assertEqual(2, result.val)
        next = result.next
        self.assertIsNone(next)
