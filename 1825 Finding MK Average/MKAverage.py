from collections import deque


class MKAverage:

    def __init__(self, m: int, k: int):
        self.q = deque(maxlen=m)
        self.k = k

    def addElement(self, num: int) -> None:
        self.q.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.q.maxlen:
            return -1
        data = list(self.q)
        data.sort()
        data = data[self.k:-self.k]
        return sum(data) // len(data)
