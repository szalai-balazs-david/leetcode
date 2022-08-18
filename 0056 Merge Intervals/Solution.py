class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for interval in intervals:
            if interval[0] > result[-1][1]:
                result.append(interval)
            else:
                if interval[1] > result[-1][1]:
                    result[-1][1] = interval[1]

        return result
