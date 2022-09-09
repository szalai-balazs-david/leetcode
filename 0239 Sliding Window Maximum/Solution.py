from collections import deque


# Cheated. Looked at discussion for alternative solution.
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        q = deque()

        def add_to_queue(i: int) -> None:
            value = nums[i]
            while q and nums[q[-1]] <= value:
                q.pop()
            q.append(i)

        for i in range(k-1):
            add_to_queue(i)

        for i in range(k-1, len(nums)):
            add_to_queue(i)
            while q[0] < i - k + 1:
                q.popleft()
            result.append(nums[q[0]])

        return result
