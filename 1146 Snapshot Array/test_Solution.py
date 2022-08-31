from unittest import TestCase
from Solution import SnapshotArray


class TestSnapshotArray(TestCase):
    def test1(self):
        x = SnapshotArray(3)
        x.set(0, 5)
        x.snap()
        x.set(0, 6)
        self.assertEqual(5, x.get(0, 0))

    def test2(self):
        x = SnapshotArray(3)
        for i in range(5):
            x.set(1, i)
            x.snap()
        x.snap()
        for i in range(6, 15):
            x.set(1, i)
            x.snap()
        self.assertEqual(4, x.get(1, 5))

    def test3(self):
        x = SnapshotArray(3)
        for i in range(5):
            x.set(1, i)
            x.snap()
        x.snap()
        for i in range(6, 14):
            x.set(1, i)
            x.snap()
        self.assertEqual(4, x.get(1, 5))

    def test4(self):
        x = SnapshotArray(3)
        for i in range(5):
            x.snap()
        x.snap()
        for i in range(6, 14):
            x.set(1, i)
            x.snap()
        self.assertEqual(0, x.get(1, 5))

    def test5(self):
        x = SnapshotArray(3)
        for i in range(5):
            x.set(1, i)
            x.snap()
        x.snap()
        for i in range(6, 14):
            x.snap()
        self.assertEqual(4, x.get(1, 13))

    def test6(self):
        x = SnapshotArray(2)
        x.set(0, 12)
        x.snap()
        x.snap()
        self.assertEqual(0, x.get(1, 0))
        self.assertEqual(0, x.get(1, 0))
        x.snap()
        x.snap()

    def test7(self):
        x = SnapshotArray(2)
        x.set(1, 16)
        x.snap()
        self.assertEqual(16, x.get(1, 0))
        x.set(1, 15)
        x.snap()
        x.set(0, 2)
        self.assertEqual(16, x.get(1, 0))
        x.snap()
        x.snap()
        x.set(1, 6)
        x.snap()
        x.set(0, 12)
        self.assertEqual(6, x.get(1, 4))
        self.assertEqual(2, x.get(0, 4))
