from queue import PriorityQueue


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        q = PriorityQueue()
        q.put(1)
        previous = 0
        i = 1

        while True:
            current = q.get()
            if current == previous:
                continue
            if i == n:
                return current
            i += 1
            q.put(current * 2)
            q.put(current * 3)
            q.put(current * 5)
            previous = current
