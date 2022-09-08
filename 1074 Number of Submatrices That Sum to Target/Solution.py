class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        print("raw matrix:")
        for row in matrix:
            print(row)
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
        print("processed matrix:")
        for row in matrix:
            print(row)
        res = 0
        for y1 in range(n):
            for y2 in range(y1, n):
                preSums = {0: 1}
                s = 0
                for x in range(m):
                    s += matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0)
                    res += preSums.get(s - target, 0)
                    print(f"y1: {y1}, y2: {y2}, x: {x}, s: {s}, res: {res}")
                    preSums[s] = preSums.get(s, 0) + 1
                print(f"start: {y1}, end: {y2}, preSums: {preSums}")
        return res
