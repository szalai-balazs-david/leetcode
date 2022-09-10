from collections import deque
from sortedcollections import SortedList


# Cheated. Had to look at discussion. Didn't know about SortedList before.
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.sorted = SortedList()
        self.q = deque()
        self.total = self.lows = self.highs = 0

    def addElement(self, num: int) -> None:
        self.total += num
        index = self.sorted.bisect_left(num)
        if index < self.k:
            self.lows += num
            if len(self.q) >= self.k:
                self.lows -= self.sorted[self.k - 1]

        if index > len(self.q) - self.k:
            self.highs += num
            if len(self.q) >= self.k:
                self.highs -= self.sorted[-self.k]

        self.q.append(num)
        self.sorted.add(num)

        if len(self.q) > self.m:
            removed = self.q.popleft()
            self.total -= removed
            index = self.sorted.index(removed)
            if index < self.k:
                self.lows -= removed
                self.lows += self.sorted[self.k]
            if index >= self.m - self.k:
                self.highs -= removed
                self.highs += self.sorted[-self.k - 1]
            self.sorted.remove(removed)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        return (self.total - self.lows - self.highs) // (self.m - 2 * self.k)
