from unittest import TestCase
from MedianFinder import MedianFinder


class TestMedianFinder(TestCase):
    def test1(self):
        x = MedianFinder()
        x.addNum(1)
        x.addNum(2)
        self.assertEqual(1.5, x.findMedian())
        x.addNum(3)
        self.assertEqual(2, x.findMedian())

    def test2(self):
        x = MedianFinder()
        for i in range(50000):
            x.addNum(i)
            self.assertEqual(i / 2, x.findMedian())

    def test3(self):
        x = MedianFinder()
        nums = [6,10,2,6,5,0,6,3,1,0,0]
        expected = [6,8,6,6,6,5.5,6,5.5,5,4,3]
        for i in range(len(nums)):
            x.addNum(nums[i])
            self.assertEqual(expected[i], x.findMedian())
