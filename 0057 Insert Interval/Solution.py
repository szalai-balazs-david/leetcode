class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        index = None
        overlapping_intervals = []

        for i in range(len(intervals)):
            interval = intervals[i]
            if index is None and interval[0] >= newInterval[0]:
                index = i
            if interval[0] <= newInterval[1] and interval[1] >= newInterval[0]:
                if index is None:
                    index = i
                overlapping_intervals.append(interval)

        if index is None:
            if len(overlapping_intervals) == 0:
                intervals.append(newInterval)
            else:
                intervals[-1] = [min(intervals[-1][0], newInterval[0]), max(intervals[-1][1], newInterval[1])]
        else:
            if len(overlapping_intervals) == 0:
                intervals.insert(index, newInterval)
            elif len(overlapping_intervals) == 1:
                intervals[index] = [min(intervals[index][0], newInterval[0]), max(intervals[index][1], newInterval[1])]
            else:
                intervals[index] = [min(overlapping_intervals[0][0], newInterval[0]), max(overlapping_intervals[-1][1], newInterval[1])]
                for i in range(1, len(overlapping_intervals)):
                    del intervals[index + 1]
        return intervals
