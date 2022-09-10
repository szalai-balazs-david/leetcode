from unittest import TestCase
from MKAverage import MKAverage


class TestMKAverage(TestCase):
    def test1(self):
        x = MKAverage(3, 1)
        x.addElement(3)
        x.addElement(1)
        self.assertEqual(-1, x.calculateMKAverage())
        x.addElement(10)
        self.assertEqual(3, x.calculateMKAverage())
        x.addElement(5)
        x.addElement(5)
        x.addElement(5)
        self.assertEqual(5, x.calculateMKAverage())

    def test2(self):
        x = MKAverage(10000, 3000)
        for i in range(20000):
            x.addElement(i)
            if i < 9999:
                self.assertEqual(-1, x.calculateMKAverage())
            else:
                self.assertEqual(i - 5000, x.calculateMKAverage())
