# Note: This is only available with subscription, so I can't actually test it with leetcode tests.
# Task as far as I understand:
# A group of two or more people wants to meet and minimize the total travel distance.
# You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group.
# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
class Solution:
    def method(self, homes: list[list[int]]) -> int:
        rows = []
        cols = []
        for i in range(len(homes)):
            for j in range(len(homes[0])):
                if homes[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        def calc_travel_dist(row: int, col: int) -> int:
            res = 0
            for i in range(len(rows)):
                res += abs(row - rows[i]) + abs(col - cols[i])
            return res

        r = round(sum(rows) / len(rows))
        c = round(sum(cols) / len(cols))

        return calc_travel_dist(r, c)
