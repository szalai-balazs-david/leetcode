from heapq import heappush, heappushpop


class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        self.odd = False

    def addNum(self, num: int) -> None:
        self.odd = not self.odd
        if self.odd:
            if len(self.high) == 0 or num <= self.high[0]:
                heappush(self.low, -num)
            else:
                num = heappushpop(self.high, num)
                heappush(self.low, -num)
        else:
            if len(self.low) == 0 or num >= -(self.low[0]):
                heappush(self.high, num)
            else:
                num = heappushpop(self.low, -num)
                heappush(self.high, -num)

    def findMedian(self) -> float:
        if self.odd:
            return -(self.low[0])
        return (self.high[0] - self.low[0]) / 2
