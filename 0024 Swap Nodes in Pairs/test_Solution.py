from unittest import TestCase
from Solution import Solution, ListNode


class TestSolution(TestCase):
    def test_swapPairs1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

        x = Solution()
        result = x.swapPairs(head)

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
        expected = [2,1,4,3]

        self.assertListEqual(expected, received)

    def test_swapPairs2(self):
        head = None

        x = Solution()
        result = x.swapPairs(head)
        self.assertIsNone(result)

    def test_swapPairs3(self):
        head = ListNode(1)

        x = Solution()
        result = x.swapPairs(head)

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

    def test_swapPairs4(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        x = Solution()
        result = x.swapPairs(head)

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

    def test_swapPairs5(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

        x = Solution()
        result = x.swapPairs(head)

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
        expected = [2,1,4,3,6,5]

        self.assertListEqual(expected, received)
