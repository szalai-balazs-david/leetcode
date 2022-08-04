from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        q = PriorityQueue()

        for num in nums:
            q.put(num * -1)

        for i in range(k - 1):
            q.get()

        return q.get() * -1
