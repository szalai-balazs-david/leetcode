from unittest import TestCase
from Solution import Solution, ListNode


class TestSolution(TestCase):
    def test_reverseKGroup1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        x = Solution()
        result = x.reverseKGroup(head, 2)

        received = []
        y = result
        i = 0
        while True:
            received.append(y.val)
            i += 1
            if i >= 10:
                break
            if y.next == None:
                break
            else:
                y = y.next
        expected = [2,1,4,3,5]

        self.assertListEqual(expected, received)

    def test_reverseKGroup2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        x = Solution()
        result = x.reverseKGroup(head, 3)

        received = []
        y = result
        i = 0
        while True:
            received.append(y.val)
            i += 1
            if i >= 10:
                break
            if y.next == None:
                break
            else:
                y = y.next
        expected = [3,2,1,4,5]

        self.assertListEqual(expected, received)

    def test_reverseKGroup3(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))

        x = Solution()
        result = x.reverseKGroup(head, 2)

        received = []
        y = result
        i = 0
        while True:
            received.append(y.val)
            i += 1
            if i >= 10:
                break
            if y.next == None:
                break
            else:
                y = y.next
        expected = [2,1,4,3,6,5,7]

        self.assertListEqual(expected, received)

    def test_reverseKGroup4(self):
        head = ListNode(1, ListNode(2))

        x = Solution()
        result = x.reverseKGroup(head, 2)

        received = []
        y = result
        i = 0
        while True:
            received.append(y.val)
            i += 1
            if i >= 10:
                break
            if y.next == None:
                break
            else:
                y = y.next
        expected = [2,1]

        self.assertListEqual(expected, received)
