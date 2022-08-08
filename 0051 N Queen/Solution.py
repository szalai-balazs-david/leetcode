class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        QUEEN = 'Q'
        HIT = 'X'
        OPEN = '.'

        def mark_hits(current: list[str], line: int, position: int):
            for j in range(line + 1, n):
                x = current[j]
                x = x[:position] + HIT + x[position+1:]
                if position - (j - line) >= 0:
                    x = x[:position-(j - line)] + HIT + x[position-(j - line)+1:]
                if position + (j - line) < n:
                    x = x[:position+(j - line)] + HIT + x[position+(j - line)+1:]
                current[j] = x

        def backtrack(results: list[list[str]], current: list[str], line: int):
            if line == n:
                result = []
                for line in current:
                    result.append(line.replace(HIT, OPEN))
                results.append(result)
                return
            if OPEN not in current[line]:
                return
            current_line = current[line]
            for i in range(n):
                if current_line[i] != OPEN:
                    continue

                current_copy = list(current)
                current_copy[line] = current_line[:i] + QUEEN + current_line[i+1:]
                mark_hits(current_copy, line, i)

                backtrack(results, current_copy, line+1)

        result = []
        current = [ OPEN*n for i in range(n)]
        backtrack(result, current, 0)

        return result
