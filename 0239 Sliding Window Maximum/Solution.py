from heapq import heappush, heappop


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        heap = [] # (-value, index). Negative value for max heap

        for i, value in enumerate(nums):
            value = nums[i]
            if heap and -value <= heap[0][0]:
                heap = [(-value, i)]
            else:
                heappush(heap, (-value, i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heappop(heap)
                result.append(-(heap[0][0]))

        return result
