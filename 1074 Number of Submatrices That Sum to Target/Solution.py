class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        sums = [[0] * (len(matrix[0]) + 1)]
        for row in matrix:
            sums.append([0] + list(row))

        for i in range(1, len(sums)):
            for j in range(1, len(sums[0])):
                sums[i][j] += sums[i][j - 1]
        for i in range(2, len(sums)):
            for j in range(1, len(sums[0])):
                sums[i][j] += sums[i - 1][j]

        # Total sum is less than target
        if target > sums[-1][-1]:
            return 0

        result = 0

        for start_i in range(1, len(sums)):
            for start_j in range(1, len(sums[0])):
                for end_i in range(start_i, len(sums)):
                    for end_j in range(start_j, len(sums[0])):
                        above = sums[start_i - 1][end_j]
                        left = sums[end_i][start_j - 1]
                        left_above = sums[start_i - 1][start_j - 1]
                        local_sum = sums[end_i][end_j] - above - left + left_above
                        if local_sum == target:
                            result += 1
        return result
