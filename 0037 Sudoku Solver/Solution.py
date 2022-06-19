class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def getLine(num: int) -> list[str]:
            return board[num]

        def getColumn(num: int) -> list[str]:
            return [row[num] for row in board]

        def getSection(x: int, y: int) -> list[str]:
            return board[x * 3][y * 3 : y * 3 + 3] + board[x * 3 + 1][y * 3 : y * 3 + 3] + board[x * 3 + 2][y * 3 : y * 3 + 3]

        def isNotDone() -> bool:
            for row in board:
                if "." in row:
                    return True
            return False

        def canItBe(x: int, y: int, target: str) -> bool:
            if target in getLine(x) or target in getColumn(y) or target in getSection(x // 3, y // 3):
                return False
            return True

        def findOptions(x: int, y: int) -> list[int]:
            options = []
            for i in range(1, 10):
                if canItBe(x, y, str(i)):
                    options.append(i)
            return options

        def tryFindValue(x: int, y: int) -> int:
            options = findOptions(x, y)

            if len(options) == 1:
                return options[0]
            else:
                for option in options:
                    s = str(option)
                    can_only_be = True
                    for row in range(9):
                        if board[row][y].isnumeric() or row == x:
                            continue
                        if canItBe(row, y, s):
                            can_only_be = False
                            break
                    if not can_only_be:
                        continue

                    for col in range(9):
                        if board[x][col].isnumeric() or col == y:
                            continue
                        if canItBe(x, col, s):
                            can_only_be = False
                            break
                    if not can_only_be:
                        continue

                    for row in range(x // 3, x // 3 + 3):
                        for col in range(y // 3, y // 3 + 3):
                            if board[row][col].isnumeric() or (row == x and col == y):
                                continue
                            if canItBe(row, col, s):
                                can_only_be = False
                                break
                    if can_only_be:
                        return option
            return -1

        def bruteForce(i: int) -> bool:
            if i == 81:
                return True
            row, col = i // 9, i % 9
            if board[row][col] == '.':
                for val in findOptions(row, col):
                    board[row][col] = str(val)
                    if bruteForce(i + 1):
                        return True
                    board[row][col] = '.'
            else:
                 if bruteForce(i + 1):
                    return True
            return False


        while isNotDone():
            found_anything = False
            for x in range(9):
                for y in range(9):
                    if board[x][y].isnumeric():
                        continue
                    a = tryFindValue(x, y)
                    if a == -1:
                        continue
                    found_anything = True
                    board[x][y] = str(a)
            if not found_anything:
                break

        if isNotDone():
            bruteForce(0)
