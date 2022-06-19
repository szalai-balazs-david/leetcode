class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if self.isBad(row):
                return False
        for i in range(9):
            column = []
            for x in range(9):
                column.append(board[x][i])
            if self.isBad(column):
                return False
        for i in range(3):
            for j in range(3):
                group = []
                for x in range(3):
                    group = group + board[i * 3 + x][j * 3 : j * 3 + 3]
                print(group)
                if self.isBad(group):
                    return False

        return True

    def isBad(self, nums: list[int]) -> bool:
        found = []
        for x in nums:
            if x == ".":
                continue
            if x in found:
                return True
            found.append(x)

        return False
